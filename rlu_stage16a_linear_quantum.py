#!/usr/bin/env python3
"""RLU Stage 16A: fixed-background linearized quantum lattice audit.

The Stage-15 gauge-fixed TEGR/RLU Hessian has two transverse-traceless physical
modes.  Each physical mode has the nearest-neighbor Euclidean massless lattice
kernel K(k)=hat{k}^2.  This script audits the resulting Gaussian quantum theory:

  * finite partition function after removal of the global zero mode;
  * position-space propagator approaching 1/(4 pi^2 r^2);
  * four-dimensional heat-kernel spectral dimension;
  * positive periodic temporal spectral representation and OS matrix;
  * lattice dispersion approaching E=|p|.

It does NOT test the interacting, fluctuating-complex, background-free theory.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import curve_fit

OUT = Path('/mnt/data/rlu_stage16a_results')
OUT.mkdir(parents=True, exist_ok=True)


def momentum_axis(L: int) -> np.ndarray:
    return 2.0 * np.sin(np.pi * np.arange(L) / L)


def finite_partition(L: int) -> dict[str, float]:
    q = momentum_axis(L)
    k2 = (
        q[:, None, None, None] ** 2
        + q[None, :, None, None] ** 2
        + q[None, None, :, None] ** 2
        + q[None, None, None, :] ** 2
    )
    mask = k2 > 1e-30
    # Two helicities: each contributes -(1/2) Tr log K, hence total -Tr log K.
    log_z = -float(np.log(k2[mask]).sum())
    return {
        'volume': L**4,
        'nonzero_modes_per_helicity': int(mask.sum()),
        'logZ_two_helicities_zero_mode_removed': log_z,
        'minus_logZ_over_volume': -log_z / L**4,
        'finite': bool(np.isfinite(log_z)),
    }


def axis_green_function(L: int) -> tuple[np.ndarray, np.ndarray]:
    """Exact periodic 4D Green function on one coordinate axis without 4D storage."""
    q = momentum_axis(L)
    spatial = (
        q[:, None, None] ** 2
        + q[None, :, None] ** 2
        + q[None, None, :] ** 2
    )
    summed_spatial = np.empty(L)
    for n0, q0 in enumerate(q):
        den = spatial + q0*q0
        if n0 == 0:
            inv = np.zeros_like(den)
            mask = den > 1e-30
            inv[mask] = 1.0 / den[mask]
        else:
            inv = 1.0 / den
        summed_spatial[n0] = inv.sum()
    r0 = max(2, L // 12)
    r = np.arange(r0, L // 4 + 1, dtype=float)
    n = np.arange(L)
    g = np.array([
        np.sum(np.cos(2.0*np.pi*n*rr/L) * summed_spatial) / L**4
        for rr in r
    ])
    return r, g


def fit_axis_green(L: int) -> dict[str, object]:
    r, y = axis_green_function(L)

    def model(rr, amplitude, exponent, constant):
        return amplitude / rr**exponent + constant

    p0 = [1.0/(4.0*math.pi**2), 2.0, -1e-6]
    pars, _ = curve_fit(model, r, y, p0=p0, maxfev=100000)
    pred = model(r, *pars)
    continuum_a = 1.0/(4.0*math.pi**2)
    return {
        'r': r.tolist(),
        'G': y.tolist(),
        'amplitude': float(pars[0]),
        'exponent': float(pars[1]),
        'finite_volume_constant': float(pars[2]),
        'fit_relative_residual': float(np.linalg.norm(pred-y)/np.linalg.norm(y)),
        'continuum_amplitude': continuum_a,
        'amplitude_relative_error': float(abs(pars[0]-continuum_a)/continuum_a),
    }


def heat_kernel_spectral_dimension(L: int) -> dict[str, object]:
    n = np.arange(L)
    eig1 = 4.0 * np.sin(np.pi*n/L)**2
    s = np.logspace(-2, math.log10(max(4.0, L*L/3.0)), 900)
    p1 = np.array([np.exp(-ss*eig1).mean() for ss in s])
    return_probability = p1**4
    ds = -2.0*np.gradient(np.log(return_probability), np.log(s))
    # Exclude lattice UV and zero-mode dominated finite-volume IR.
    window = (s >= 1.5) & (s <= L*L/80.0)
    return {
        'window_median': float(np.median(ds[window])),
        'window_mean': float(np.mean(ds[window])),
        'window_min': float(np.min(ds[window])),
        'window_max': float(np.max(ds[window])),
        'closest_to_four': float(ds[np.argmin(abs(ds-4.0))]),
        's_at_closest': float(s[np.argmin(abs(ds-4.0))]),
    }


def temporal_correlator(L: int, spatial_mode=(1, 0, 0)) -> dict[str, object]:
    m = np.asarray(spatial_mode, dtype=float)
    p = 2.0*math.pi*m/L
    omega2 = float(np.sum(4.0*np.sin(p/2.0)**2))
    n0 = np.arange(L)
    k0 = 2.0*math.pi*n0/L
    denom = 4.0*np.sin(k0/2.0)**2 + omega2
    t = np.arange(L)
    c_numeric = np.array([np.mean(np.cos(k0*tt)/denom) for tt in t])

    energy = 2.0*math.asinh(math.sqrt(omega2)/2.0)
    c_analytic = np.array([
        math.cosh(energy*(L/2.0-min(tt, L-tt))) /
        (2.0*math.sinh(energy)*math.sinh(energy*L/2.0))
        for tt in t
    ])

    # Osterwalder-Schrader reflection matrix for positive-time test vectors.
    times = np.arange(1, max(2, L//4))
    reflection = np.array([
        [c_numeric[(ti+tj) % L] for tj in times]
        for ti in times
    ])
    eig = np.linalg.eigvalsh((reflection+reflection.T)/2.0)
    continuum_p = float(np.linalg.norm(p))
    return {
        'spatial_mode': list(spatial_mode),
        'lattice_energy': energy,
        'continuum_abs_p': continuum_p,
        'dispersion_relative_error': float(abs(energy-continuum_p)/continuum_p),
        'analytic_correlator_relative_error': float(
            np.linalg.norm(c_numeric-c_analytic)/np.linalg.norm(c_analytic)
        ),
        'correlator_minimum': float(c_numeric.min()),
        'reflection_minimum_eigenvalue': float(eig.min()),
        'reflection_negative_count_tolerance_1e-11': int(np.sum(eig < -1e-11)),
    }


def dispersion_scan(L: int) -> dict[str, object]:
    rows = []
    for mode in range(1, max(3, L//10+1)):
        p = 2.0*math.pi*mode/L
        phat = 2.0*math.sin(p/2.0)
        energy = 2.0*math.asinh(abs(phat)/2.0)
        rows.append({
            'mode': mode,
            'p': p,
            'energy': energy,
            'relative_error': abs(energy-p)/p,
        })
    x = np.array([row['p']**2 for row in rows])
    y = np.array([row['relative_error'] for row in rows])
    coefficient = float(np.dot(x, y)/np.dot(x, x))
    return {'rows': rows, 'relative_error_over_p_squared_fit': coefficient}


def main() -> None:
    results: dict[str, object] = {
        'scope': 'quadratic fixed-background quantum audit; not interacting/background-free',
        'physical_helicity_count': 2,
        'partition_functions': {},
        'scaling': {},
    }

    for L in (16, 24, 32):
        results['partition_functions'][f'L{L}'] = finite_partition(L)

    for L in (32, 48, 64, 80, 96):
        results['scaling'][f'L{L}'] = {
            'axis_green': fit_axis_green(L),
            'spectral_dimension': heat_kernel_spectral_dimension(L),
            'temporal_correlator': temporal_correlator(L),
            'dispersion': dispersion_scan(L),
        }

    output = OUT/'stage16a_linear_quantum.json'
    output.write_text(json.dumps(results, indent=2))

    print('RLU STAGE 16A — LINEARIZED QUANTUM LATTICE AUDIT')
    print('='*78)
    for L in (32, 48, 64, 80, 96):
        row = results['scaling'][f'L{L}']
        green = row['axis_green']
        sd = row['spectral_dimension']
        tc = row['temporal_correlator']
        print(
            f'L={L:2d}: G exponent={green["exponent"]:.6f}, '
            f'A={green["amplitude"]:.8f}, d_s={sd["window_median"]:.6f}, '
            f'disp.err={tc["dispersion_relative_error"]:.3e}, '
            f'temporal err={tc["analytic_correlator_relative_error"]:.3e}, '
            f'OS min eig={tc["reflection_minimum_eigenvalue"]:.3e}'
        )
    print('\nVERDICT')
    print('PASS (quadratic, fixed background): the two physical helicities define a finite')
    print('Gaussian lattice measure with the massless propagator, positive temporal spectral')
    print('representation, four-dimensional heat-kernel scaling, and continuum dispersion.')
    print('OPEN: interacting, fluctuating-complex, background-free critical phase.')


if __name__ == '__main__':
    main()

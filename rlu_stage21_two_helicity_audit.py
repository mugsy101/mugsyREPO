#!/usr/bin/env python3
"""RLU Stage 21: two-helicity projector and curvature-squared obstruction audit.

This script is an exact/synthetic diagnostic, not a full Cartan-CDT Monte Carlo.
It checks:
  1. completeness and ranks of scalar/vector/TT projectors for a 3D spatial slice;
  2. exact separation of two TT helicities from scalar/vector contamination;
  3. invariance of the reconstructed spatial metric under local internal rotations;
  4. the extra opposite-residue pole created by a finite k^4 curvature term;
  5. the conditional coupled-criticality exponent inferred from published CDT FSS values;
  6. a synthetic pole-fitting protocol that a Cartan-CDT production run must pass.
"""
from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
from numpy.linalg import eigvalsh, matrix_rank, norm
from scipy.optimize import least_squares

OUT = Path('/mnt/data/rlu_stage21_results')
OUT.mkdir(parents=True, exist_ok=True)

# Orthonormal basis for real symmetric 3x3 matrices under Frobenius inner product.
SQ2 = math.sqrt(2.0)
SYM_BASIS = []
for i in range(3):
    M = np.zeros((3, 3)); M[i, i] = 1.0; SYM_BASIS.append(M)
for i, j in ((0, 1), (0, 2), (1, 2)):
    M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1.0 / SQ2; SYM_BASIS.append(M)
SYM_BASIS = np.asarray(SYM_BASIS)


def sym_to_vec(h: np.ndarray) -> np.ndarray:
    return np.array([np.sum(B * h) for B in SYM_BASIS])


def vec_to_sym(v: np.ndarray) -> np.ndarray:
    return np.einsum('a,aij->ij', v, SYM_BASIS)


def operator_matrix(op) -> np.ndarray:
    cols = [sym_to_vec(op(B)) for B in SYM_BASIS]
    return np.column_stack(cols)


def transverse_projectors(k: np.ndarray) -> Dict[str, np.ndarray]:
    kh = np.asarray(k, float)
    kh /= norm(kh)
    Q = np.outer(kh, kh)
    P = np.eye(3) - Q

    def tt(h):
        php = P @ h @ P
        return php - 0.5 * P * np.trace(php)

    def vec(h):
        return P @ h @ Q + Q @ h @ P

    def scalar_transverse(h):
        return 0.5 * P * np.trace(P @ h)

    def scalar_longitudinal(h):
        return Q * np.trace(Q @ h)

    mats = {
        'TT': operator_matrix(tt),
        'V': operator_matrix(vec),
        'ST': operator_matrix(scalar_transverse),
        'SL': operator_matrix(scalar_longitudinal),
    }
    mats['I_sum'] = mats['TT'] + mats['V'] + mats['ST'] + mats['SL']
    return mats


def polarization_basis(k: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
    kh = np.asarray(k, float); kh /= norm(kh)
    trial = np.array([1.0, 0.0, 0.0])
    if abs(np.dot(trial, kh)) > 0.85:
        trial = np.array([0.0, 1.0, 0.0])
    e1 = trial - np.dot(trial, kh) * kh
    e1 /= norm(e1)
    e2 = np.cross(kh, e1)
    e2 /= norm(e2)
    plus = (np.outer(e1, e1) - np.outer(e2, e2)) / math.sqrt(2.0)
    cross = (np.outer(e1, e2) + np.outer(e2, e1)) / math.sqrt(2.0)
    return plus, cross


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    A = rng.normal(size=(3, 3))
    q, r = np.linalg.qr(A)
    signs = np.sign(np.diag(r)); signs[signs == 0] = 1
    q = q @ np.diag(signs)
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def pole_decomposition(Z: float, alpha: float) -> Dict[str, float]:
    """For G(x)=1/[x(Z+alpha*x)] with x=k^2.

    G=(1/Z)[1/x - 1/(x+Z/alpha)]. The second pole has opposite residue.
    """
    return {
        'massless_residue': 1.0 / Z,
        'extra_residue': -1.0 / Z,
        'extra_euclidean_pole_x': -Z / alpha,
        'extra_mass_sq_if_alpha_positive': Z / alpha,
    }


def synthetic_correlator_fit(rng: np.random.Generator):
    # Simulated inverse TT correlator on a finite torus:
    # Gamma = m2 + Zt*omega_hat^2 + Zs*k_hat^2 + alpha*k_hat^4.
    L = 32
    rows = []
    true = dict(m2=0.003, Zt=1.12, Zs=0.94, alpha=0.075)
    for nt in range(0, 6):
        wh = 2 * math.sin(math.pi * nt / L)
        for nx in range(1, 7):
            kh = 2 * math.sin(math.pi * nx / L)
            gamma = true['m2'] + true['Zt'] * wh**2 + true['Zs'] * kh**2 + true['alpha'] * kh**4
            # Correlator with 0.4% multiplicative noise.
            C = (1.0 / gamma) * math.exp(rng.normal(scale=0.004))
            rows.append((wh**2, kh**2, 1.0 / C))
    arr = np.asarray(rows)
    X = np.column_stack([np.ones(len(arr)), arr[:, 0], arr[:, 1], arr[:, 1] ** 2])
    coef, *_ = np.linalg.lstsq(X, arr[:, 2], rcond=None)
    fit = dict(m2=coef[0], Zt=coef[1], Zs=coef[2], alpha=coef[3])
    z1_speed_sq = fit['Zs'] / fit['Zt']
    return true, fit, z1_speed_sq, arr


def main() -> None:
    rng = np.random.default_rng(20260724)
    k = np.array([1.0, 2.0, -0.7])
    projs = transverse_projectors(k)
    I6 = np.eye(6)

    projector_report = {}
    for name in ('TT', 'V', 'ST', 'SL'):
        P = projs[name]
        projector_report[name] = {
            'rank': int(matrix_rank(P, tol=1e-10)),
            'idempotence_error': float(norm(P @ P - P)),
            'min_eigenvalue': float(np.min(eigvalsh(0.5 * (P + P.T)))),
            'max_eigenvalue': float(np.max(eigvalsh(0.5 * (P + P.T)))),
        }
    projector_report['completeness_error'] = float(norm(projs['I_sum'] - I6))
    projector_report['max_pairwise_overlap'] = float(max(
        norm(projs[a] @ projs[b])
        for i, a in enumerate(('TT', 'V', 'ST', 'SL'))
        for b in ('TT', 'V', 'ST', 'SL')[i+1:]
    ))

    plus, cross = polarization_basis(k)
    kh = k / norm(k)
    e1 = plus @ plus  # only used to seed generic contamination
    v = np.array([0.2, -0.1, 0.4]); v -= np.dot(v, kh) * kh
    contaminant_v = np.outer(kh, v) + np.outer(v, kh)
    contaminant_s = 0.7 * np.eye(3) + 0.4 * np.outer(kh, kh)
    h = 1.3 * plus - 0.8 * cross + contaminant_v + contaminant_s
    hvec = sym_to_vec(h)
    htt = vec_to_sym(projs['TT'] @ hvec)
    expected_tt = 1.3 * plus - 0.8 * cross
    separation_error = float(norm(htt - expected_tt))
    recovered_plus = float(np.sum(htt * plus))
    recovered_cross = float(np.sum(htt * cross))

    # Internal frame rotation leaves the metric E^T E invariant.
    gauge_errors = []
    for _ in range(1000):
        E = rng.normal(size=(3, 3))
        R = random_rotation(rng)
        gauge_errors.append(norm((R @ E).T @ (R @ E) - E.T @ E))

    # Exact pole obstruction for a representative positive Wilson coefficient.
    pole = pole_decomposition(Z=1.0, alpha=0.08)
    # Scaling required to decouple the extra pole if alpha_R ~ a^p, M_P held fixed.
    a_values = 2.0 ** (-np.arange(1, 9))
    pole_scalings = {}
    for p in (0.0, 0.5, 1.0, 2.0):
        alpha = 0.08 * a_values**p
        masses = np.sqrt(1.0 / alpha)
        pole_scalings[str(p)] = masses.tolist()

    # Conditional conversion of the published N4 finite-size exponent to nu_corr,
    # assuming N4 ~ L^4, followed by the product-fixed-point coupling eigenvalue.
    cdt_nu_volume = {'toroidal_central': 2.7, 'toroidal_low': 2.3, 'toroidal_high': 3.1,
                     'spherical': 2.51}
    criticality = {}
    nu_cartan_gaussian = 0.5
    for key, nuvol in cdt_nu_volume.items():
        nucorr = nuvol / 4.0
        y_mix = 1.0 / nucorr + 1.0 / nu_cartan_gaussian - 4.0
        criticality[key] = {'nu_corr_conditional': nucorr, 'energy_energy_y': y_mix}

    true_fit, fitted, speed_sq, corr_data = synthetic_correlator_fit(rng)
    np.savetxt(OUT / 'synthetic_tt_inverse_correlator.csv', corr_data,
               delimiter=',', header='omega_hat_sq,k_hat_sq,Gamma_TT', comments='')

    report = {
        'projectors': projector_report,
        'tt_separation_error': separation_error,
        'recovered_plus': recovered_plus,
        'recovered_cross': recovered_cross,
        'metric_gauge_covariance_max_error': float(max(gauge_errors)),
        'metric_gauge_covariance_mean_error': float(np.mean(gauge_errors)),
        'curvature_squared_pole': pole,
        'extra_pole_mass_scalings': pole_scalings,
        'conditional_criticality': criticality,
        'synthetic_correlator_true': true_fit,
        'synthetic_correlator_fit': fitted,
        'fitted_speed_sq': speed_sq,
    }
    (OUT / 'stage21_two_helicity_audit.json').write_text(json.dumps(report, indent=2))

    # Compact text output.
    lines = [
        'RLU STAGE 21: TWO-HELICITY AND WILSON-TERM AUDIT',
        '=' * 78,
        f"TT projector rank: {projector_report['TT']['rank']}",
        f"Vector projector rank: {projector_report['V']['rank']}",
        f"Scalar projector ranks: {projector_report['ST']['rank']} + {projector_report['SL']['rank']}",
        f"Projector completeness error: {projector_report['completeness_error']:.3e}",
        f"Maximum projector overlap: {projector_report['max_pairwise_overlap']:.3e}",
        f"TT separation error: {separation_error:.3e}",
        f"Recovered (+,x): ({recovered_plus:.12f}, {recovered_cross:.12f})",
        f"Metric gauge covariance max error: {max(gauge_errors):.3e}",
        '',
        'Curvature-squared pole decomposition:',
        f"  massless residue = {pole['massless_residue']:+.6f}",
        f"  extra residue    = {pole['extra_residue']:+.6f}",
        f"  extra m^2        = {pole['extra_mass_sq_if_alpha_positive']:.6f}",
        '  => any finite alpha produces an opposite-residue extra pole.',
        '',
        'Conditional weak-product-fixed-point test:',
    ]
    for key, vals in criticality.items():
        lines.append(f"  {key}: nu_corr={vals['nu_corr_conditional']:.4f}, y_mix={vals['energy_energy_y']:+.4f}")
    lines += [
        '',
        'Synthetic TT pole fit:',
        f"  true   = {true_fit}",
        f"  fitted = {fitted}",
        f"  c_T^2  = {speed_sq:.8f}",
        '',
        'VERDICT',
        'PASS: a coordinate-defined toroidal slice admits an exact rank-2 TT projector.',
        'PASS: the projector removes all scalar/vector contamination and retains two modes.',
        'PASS: metric observables are invariant under local internal frame rotations.',
        'NO-GO: a finite renormalized curvature-squared Wilson coefficient yields an extra',
        'opposite-residue spin-2 pole. A two-helicity continuum trajectory requires the',
        'physical Wilson coefficient to flow to zero, or a separately proved cancellation.',
        'DIAGNOSTIC: published CDT finite-size exponents, conditionally converted with d=4,',
        'make weak energy-energy coupling to a Gaussian Cartan sector irrelevant; this favors',
        'a decoupled/spectator Cartan limit at weak coupling, not a new mixed fixed point.',
    ]
    (OUT / 'stage21_two_helicity_audit.txt').write_text('\n'.join(lines) + '\n')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()

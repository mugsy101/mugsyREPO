#!/usr/bin/env python3
"""RLU Stage 23: single-metric locking and relative spin-2 decoupling audit.

The CDT triangulation and the Cartan coframe each define a metric-like tensor.
At quadratic TT level this is a two-field system. This script diagonalizes the
most general minimal kinetic+Fierz-Pauli locking kernel and maps the conditions
for an effective two-helicity infrared limit.
"""
from __future__ import annotations
import json, math
from pathlib import Path
import numpy as np
import pandas as pd
from numpy.linalg import eigvalsh

OUT=Path('/mnt/data/rlu_stage23_results');OUT.mkdir(exist_ok=True)

def tensor_kernel(k2,Zr,Zc,mrel2,alpha=0.0):
    # One copy for each TT polarization. h_R is Regge/CDT metric, h_C Cartan metric.
    return np.array([[Zr*k2+mrel2, -mrel2],
                     [-mrel2, Zc*k2+mrel2+alpha*k2*k2]],float)

def analytic_low_k_masses(Zr,Zc,mrel2):
    # At alpha=0, canonical fields sqrt(Z) h; relative mass eigenvalue.
    if Zr<=0 or Zc<=0: return math.nan
    return mrel2*(1/Zr+1/Zc)

def main():
    rows=[]
    Zr=1.0;Zc=0.8
    for mrel2 in (0.0,0.01,0.1,1.0,10.0,100.0):
      for alpha in (0.0,0.05):
       for k in (1e-4,0.02,0.1,0.5):
        vals=eigvalsh(tensor_kernel(k*k,Zr,Zc,mrel2,alpha))
        rows.append({'mrel2':mrel2,'alpha':alpha,'k':k,'eig_low':vals[0],'eig_high':vals[1],
                     'relative_mass_sq_canonical':analytic_low_k_masses(Zr,Zc,mrel2)})
    pd.DataFrame(rows).to_csv(OUT/'two_metric_tt_eigenvalues.csv',index=False)

    # Continuum scaling m_rel * xi for mrel2(a) ~ a^{-p}, xi/a ~ a^{-1} at fixed physical xi.
    a=2.0**(-np.arange(1,10))
    scaling=[]
    for p in (-2,-1,0,1,2):
        # mrel^2 in lattice units = c*a^p. Physical dimensionless mrel*xi uses xi_latt~1/a.
        m2=0.2*a**p
        mxi=np.sqrt(m2*(1/Zr+1/Zc))/a
        for ai,m2i,mx in zip(a,m2,mxi):
            scaling.append({'p':p,'a':ai,'mrel2_lattice':m2i,'mrel_times_xi':mx})
    pd.DataFrame(scaling).to_csv(OUT/'relative_mode_decoupling_scaling.csv',index=False)

    # Auxiliary Cartan limit: Zc -> 0 at fixed algebraic locking. Integrate out h_C.
    # Schur complement Gamma_eff = A-B^2/C.
    aux=[]
    for Zc0 in (1.0,0.1,0.01,1e-4,0.0):
      for k in (0.01,0.1,0.5):
        k2=k*k;m=2.0
        A=Zr*k2+m;B=-m;C=Zc0*k2+m
        Geff=A-B*B/C
        aux.append({'Zc':Zc0,'k':k,'Gamma_eff':Geff,'Gamma_GR':Zr*k2,
                    'relative_error':abs(Geff-Zr*k2)/(Zr*k2)})
    pd.DataFrame(aux).to_csv(OUT/'auxiliary_cartan_schur_limit.csv',index=False)

    summary={
      'mode_count_no_locking':'two independent TT fields => 4 massless helicities',
      'mode_count_finite_locking':'one massless diagonal tensor (2 helicities) plus one relative massive tensor (5 Lorentzian polarizations after nonlinear FP completion)',
      'two_helicity_IR_condition':'m_relative * xi -> infinity, or Cartan kinetic residue Z_C -> 0 so the Cartan metric is auxiliary',
      'finite_wilson_condition':'alpha/(Z*xi^2) -> 0 and extra pole mass*xi -> infinity',
      'exact_auxiliary_limit':'with Z_C=0, integrating out h_C gives Gamma_eff=Z_R k^2 exactly',
    }
    (OUT/'single_metric_locking_summary.json').write_text(json.dumps(summary,indent=2))
    text='''RLU STAGE 23: SINGLE-METRIC LOCKING AUDIT
==============================================================================
NO LOCKING:
  The CDT/Regge tensor and Cartan tensor are independent: two massless TT fields,
  hence four helicities.

FINITE FIERZ-PAULI LOCKING:
  The diagonal combination remains massless (two helicities), but the relative
  tensor is massive. In a nonlinear completion it carries five physical spin-2
  polarizations. This is not a strict two-helicity theory at finite energy.

CONTROLLED TWO-HELICITY LIMITS:
  (A) m_relative * xi -> infinity, so every relative tensor pole decouples;
  (B) Z_C -> 0 with algebraic locking, so the Cartan metric is auxiliary.
  The Schur complement then equals Z_R k^2 exactly.

ADDITIONAL WILSON GATE:
  alpha_4/(Z_T xi^2) -> 0, equivalently m_extra*xi -> infinity.

VERDICT:
  Generic Cartan-CDT is not a two-helicity model. The candidate universal
  trajectory is a single-metric locking/decoupling surface.
'''
    (OUT/'single_metric_locking_summary.txt').write_text(text)
    print(text)

if __name__=='__main__':main()

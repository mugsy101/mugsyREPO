# RLU Stage 25 — Cartan-CDT Universal Two-Helicity Production Protocol

## Hypothesis

There exists a continuous critical trajectory in the enlarged Cartan-CDT coupling space, reachable from the extended de Sitter side, on which:

1. the Cartan and Regge metrics lock into one infrared metric;
2. torsion and relative-metric modes decouple;
3. the physical curvature-squared coefficient vanishes in units of the diverging correlation length;
4. exactly two positive-residue massless TT channels survive;
5. the infrared geometry is four-dimensional and the torsion action flows to TEGR.

## Revised action

\[
S=S_{\rm CDT}+S_\kappa+S_{\rm frame}+S_{\rm match}+S_T+S_{\rm MM}+S_{W,\rm reg}.
\]

The locking terms are mandatory rather than optional diagnostics.

### Shape locking

\[
S_{\rm match}=\lambda_M\sum_i
\|K_i-\ell_C^2K^{\rm CDT}_{\operatorname{type}(i)}\|^2.
\]

### Shared-tetrahedron compatibility

For each adjacent simplex pair \(i,j\), compare the induced three-metric on their common tetrahedron after Cartan transport. Penalize their difference by a gauge-invariant Frobenius norm.

### Torsion control

\[
S_T=\lambda_T\sum_f\|\Theta_f\|^2.
\]

### Curvature regulator

Retain the Wilson term only as a regulator. Measure its renormalized TT coefficient and require

\[
\alpha_4/(Z_T\xi^2)\to0.
\]

## Geometry ensembles

Run both:

- \(S^1\times S^3\) spacetime topology;
- \(S^1\times T^3\) spacetime topology.

The toroidal ensemble is required for the cleanest harmonic-coordinate helicity decomposition.

## Couplings

Scan

\[
(k_0,\Delta;\kappa,\beta,\gamma_{\rm reg},\lambda_M,\lambda_T).
\]

Use the homogeneous line \(\beta/\gamma\approx-1/16\) only as an initial seed.

## Candidate surfaces

1. Cartan-deformed \(C_{\rm dS}-C_b\) surface.
2. A possible critical endpoint of the \(C_{\rm dS}-A\) first-order surface.
3. Intersections with metric-locking and torsion-decoupling surfaces.

## Sampler

Alternate:

- causal triangulation moves;
- local and overrelaxed \(V_i\) updates;
- heat-bath or Metropolis \(SO(5)\) link updates;
- replica swaps in \(\Delta,\beta,\lambda_M\);
- multicanonical biasing in the strongest coexistence observable.

Run independent hot, cold, de Sitter-seeded, and bifurcation-seeded chains.

## Measurements

### Thermodynamics

- action and component histograms;
- latent heat;
- Binder cumulants;
- free-energy barrier scaling;
- integrated autocorrelation times;
- replica round trips.

### Geometry

- de Sitter volume profile and covariance;
- Hausdorff dimension;
- spectral dimension;
- graph diameter and Laplacian gap;
- baby-universe/minimal-neck statistics;
- curvature distributions.

### Cartan locking

- local Gram mismatch;
- shared-face metric mismatch;
- relative-metric correlation length;
- Cartan kinetic residue \(Z_C\);
- relative-mode mass \(m_{\rm rel}\).

### Torsion

- loop-closure torsion norm;
- spin-projected torsion correlators;
- torsion gap;
- flow of \((I_1,I_2,I_3)\) to the TEGR ray.

### Helicity

Use harmonic toroidal coordinates, reconstruct \(g_{ij}(x,t)\), Fourier transform, and project with the exact TT/vector/scalar projectors.

Fit

\[
\Gamma_{\rm TT}=m_T^2+Z_t\hat\omega^2+Z_s\hat k^2+\alpha_4\hat k^4+\cdots.
\]

Perform a generalized eigenvalue analysis of the full correlator matrix, not only separate channel fits.

## Finite-size ladder

A credible first ladder is

\[
N_4\in\{4\times10^4,8\times10^4,1.6\times10^5,3.2\times10^5\},
\]

with at least two time extents at each volume. Smaller lattices are calibration only.

## Blind analysis

Pre-register:

- fit windows;
- eigenvalue thresholds;
- continuum extrapolation forms;
- pass/kill thresholds;
- excluded thermalization intervals.

Keep one volume and one topology blinded until the analysis pipeline is fixed.

## Necessary limits

\[
\xi/a\to\infty,
\quad
d_s^{\rm IR}\to4,
\quad
D(N)\sim N^{1/4},
\quad
\lambda_1\sim N^{-1/2},
\]

\[
m_TL\to0,
\quad
N_{\rm light,TT}=2,
\quad
N_{\rm light,nonTT}=0,
\]

\[
m_{\rm rel}\xi\to\infty\ \text{or}\ Z_C/Z_R\to0,
\quad
m_{\rm torsion}\xi\to\infty,
\]

\[
\alpha_4/(Z_T\xi^2)\to0,
\quad
c_T^2=Z_s/Z_t\to1,
\quad
(q_1,q_2,q_3)\to(1,2,-4).
\]

## Immediate kill conditions

- persistent bimodality with barrier proportional to volume;
- two independent massless TT pairs;
- finite opposite-residue \(k^4\) pole;
- light relative massive-spin-2 state;
- light torsion or scalar channel;
- failure of de Sitter-side four-dimensional scaling;
- topology-dependent continuum exponents;
- negative transfer-matrix spectral weight.

## Interpretation rule

A continuous thermodynamic transition is necessary but not sufficient. A four-dimensional spectral plateau is necessary but not sufficient. The theory passes only when the pole and residue count itself approaches one massless spin-2 representation with two helicities.

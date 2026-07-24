# RLU Stages 21–24 — Cartan-CDT and the Universal Two-Helicity Question

## Scientific status

This report asks the decisive question for the surviving microscopic branch of Relational Link Unification (RLU-C4):

> Does Cartan-decorated four-dimensional Causal Dynamical Triangulations (Cartan-CDT) possess a universal critical trajectory whose Lorentzian infrared spectrum contains exactly the two helicities of one massless graviton and no additional scalar, vector, torsion, or spin-2 poles?

The present answer is:

\[
\boxed{\text{Not established by existing CDT data or by the current Cartan-CDT action.}}
\]

However, the analysis does identify a sharply constrained candidate surface and supplies the exact observables needed to confirm or kill it:

\[
\boxed{
\text{continuous geometric criticality}
+\text{single-metric locking}
+\text{torsion decoupling}
+\alpha_{4,\rm phys}\to0
}
\]

where \(\alpha_{4,\rm phys}\) is the physical curvature-squared coefficient that produces the \(k^4\) part of the transverse-traceless inverse propagator.

No full four-dimensional Cartan-CDT production ensemble was simulated in this stage. Publicly accessible code located during this audit covered lower-dimensional CDT, not a ready-made four-dimensional production ensemble with configurations and move machinery. The numerical work reported here therefore consists of exact projector and pole audits, a fixed-complex Cartan control, a two-metric locking calculation, and a synthetic end-to-end validation of the proposed helicity observable.

---

## 1. What pure CDT currently establishes

Four-dimensional CDT has a finite Wick-rotated path integral, a de Sitter-like extended phase with four-dimensional large-scale volume scaling, and numerical indications consistent with a possible ultraviolet fixed point. Existing publications do not yet provide a direct nonperturbative measurement showing exactly two graviton helicities. The most developed observables concern spatial volume, scale-factor fluctuations, spectral dimension, quantum curvature, topology, and coordinate constructions.

The critical-line situation is not yet a complete solution:

1. The physically extended phase is \(C_{\rm dS}\).
2. The \(C_{\rm dS}-C_b\) and \(C_b-B\) transitions have evidence of second- or higher-order behavior.
3. The \(C_{\rm dS}-A\) transition has generally been classified as first order in the established phase diagram, although recent renormalization analyses report scaling behavior toward that region that may be compatible with a UV interpretation and explicitly state that more precision is required.
4. Neither the existence of a continuous transition nor four-dimensional volume scaling by itself proves a two-helicity graviton spectrum.

Thus pure CDT supplies a promising geometry ensemble but not the requested helicity theorem.

---

## 2. Exact spin decomposition on a toroidal slice

A toroidal spatial topology permits harmonic scalar coordinates. For a nonzero spatial momentum \(\mathbf k\), define

\[
P_{ij}=\delta_{ij}-\hat k_i\hat k_j.
\]

The transverse-traceless projector on symmetric spatial tensors is

\[
\Lambda^{\rm TT}_{ij,kl}
=\frac12\left(P_{ik}P_{jl}+P_{il}P_{jk}-P_{ij}P_{kl}\right).
\]

Together with vector, transverse-scalar, and longitudinal-scalar projectors, this decomposes the six components of a symmetric three-tensor into

\[
6=2_{\rm TT}+2_{\rm V}+1_{\rm ST}+1_{\rm SL}.
\]

The exact audit gave:

| Quantity | Result |
|---|---:|
| TT projector rank | 2 |
| Vector projector rank | 2 |
| Scalar projector ranks | 1 and 1 |
| Completeness error | \(3.852\times10^{-16}\) |
| Maximum pairwise overlap | \(1.439\times10^{-16}\) |
| Synthetic TT separation error | \(4.535\times10^{-16}\) |
| Internal-frame metric covariance error | \(1.228\times10^{-14}\) |

A synthetic tensor containing plus and cross amplitudes \((1.3,-0.8)\), together with scalar and vector contamination, was projected back to

\[
(1.3000000000000003,-0.8).
\]

This proves that a two-helicity observable can be defined on toroidal CDT configurations once relational spatial coordinates and a local metric estimator are supplied. It does not prove that the measured interacting ensemble has only those two light channels.

---

## 3. The Wilson-curvature obstruction

The current Cartan-CDT action contains

\[
S_W=\gamma\sum_f\left[5-\operatorname{Tr}H_f\right].
\]

Its small-cell continuum expansion contains a Yang-Mills-type Cartan curvature term

\[
\int d^4x\sqrt g\,F^{AB}_{\mu\nu}F_{AB}^{\mu\nu}.
\]

In the broken Cartan phase,

\[
F^{IJ}=R^{IJ}-\ell^{-2}e^I\wedge e^J,
\qquad
F^{I5}=\ell^{-1}T^I,
\]

so the Wilson term contains, up to convention-dependent coefficients,

\[
R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma},
\qquad
T^2,
\qquad
R,
\qquad
\text{and a constant term}.
\]

The MacDowell-Mansouri contribution supplies the Euler density, Einstein term, and cosmological term. Its Euler term is topological and cannot cancel the dynamical non-topological part of \(R_{\mu\nu\rho\sigma}^2\).

For a transverse-traceless perturbation, the inverse propagator has the generic form

\[
\Gamma_{\rm TT}(k^2)=Z_Tk^2+\alpha_4k^4.
\]

If treated as a fundamental finite higher-derivative theory,

\[
\frac1{k^2(Z_T+\alpha_4k^2)}
=\frac1{Z_T}
\left[
\frac1{k^2}-\frac1{k^2+Z_T/\alpha_4}
\right].
\]

The second pole has the opposite residue. If \(\alpha_4<0\), it is also tachyonic in the simple local truncation. If the action is treated only as an effective field theory, this pole may lie beyond the cutoff and should not be retained nonperturbatively; nevertheless, a universal fundamental continuum trajectory with only two physical helicities must make it decouple.

The required scaling condition is

\[
\boxed{
\frac{\alpha_{4,\rm phys}}{Z_T\xi^2}\longrightarrow0,
\qquad
m_{\rm extra}\xi\longrightarrow\infty.
}
\]

The symbolic curvature audit found, for TT amplitudes \(a,b\),

\[
R_{\mu\nu\rho\sigma}^2
=2k^4(a^2+b^2),
\qquad
R_{\mu\nu}^2
=\frac12k^4(a^2+b^2),
\qquad
R^2=0,
\]

while the Gauss-Bonnet quadratic contribution vanishes, as expected for a topological term. Therefore the existing Wilson coupling is not automatically harmless.

---

## 4. The double-metric obstruction

CDT already carries a Regge metric through its simplicial edge lengths and connectivity. Independent Cartan coframes define a second local metric. Unless an explicit compatibility condition locks them, the theory is generically bimetric.

A representative TT quadratic kernel is

\[
\Gamma_{\rm TT}(k)=
\begin{pmatrix}
Z_Rk^2+m_{\rm rel}^2 & -m_{\rm rel}^2\\
-m_{\rm rel}^2 & Z_Ck^2+m_{\rm rel}^2+\alpha_4k^4
\end{pmatrix}.
\]

Three cases follow.

### No locking

For \(m_{\rm rel}=0\), both metrics possess a massless TT tensor:

\[
2+2=4\text{ massless helicities}.
\]

### Finite Fierz-Pauli locking

One diagonal tensor remains massless, while the relative tensor becomes massive. A consistent nonlinear massive-spin-2 completion carries five Lorentzian polarizations. This is a healthy effective bimetric possibility, but not a strict two-helicity theory at finite energy.

### Strict two-helicity infrared limit

The relative mode must disappear through either

\[
\boxed{m_{\rm rel}\xi\to\infty}
\]

or

\[
\boxed{Z_C\to0}
\]

with algebraic metric locking, making the Cartan metric auxiliary. In the exact auxiliary limit, integrating out the Cartan tensor gives

\[
\Gamma_{\rm eff}=Z_Rk^2.
\]

Therefore generic Cartan-CDT is not a two-helicity theory. A candidate two-helicity trajectory is a single-metric locking or decoupling surface.

---

## 5. The action must be revised

The prior local frame term enforces nondegenerate coframes but is globally topology-blind and does not force the Cartan metric to agree with the CDT simplex geometry. A production action aimed at two helicities needs explicit compatibility terms.

A minimal revised action is

\[
S_{\rm 2h}=S_{\rm CDT}
+S_\kappa
+S_{\rm frame}
+S_{\rm match}
+S_T
+S_{\rm MM}
+S_{W,\rm reg}.
\]

Here

\[
S_{\rm match}
=\lambda_M\sum_i
\left\|
K_i-\ell_C^2K^{\rm CDT}_{\operatorname{type}(i)}
\right\|^2,
\]

where \(K_i\) is the Cartan coframe Gram matrix and \(K^{\rm CDT}_{\operatorname{type}(i)}\) is the target Gram matrix for the local CDT simplex type.

A discrete compatibility term should require transported coframes to induce the same shared-tetrahedron geometry from both adjacent four-simplices. A torsion-suppression term is

\[
S_T=\lambda_T\sum_f\|\Theta_f\|^2.
\]

The Wilson term may be retained as a finite-cutoff stabilizer, but its physical renormalized coefficient must satisfy the decoupling condition above. Alternatively, the curvature regulator must be replaced by an action whose surviving curvature-squared part is purely topological.

The key continuum conditions are therefore

\[
\lambda_M\xi^{y_M}\to\infty,
\qquad
\lambda_T\xi^{y_T}\to\infty,
\qquad
\frac{\alpha_{4,\rm phys}}{Z_T\xi^2}\to0.
\]

---

## 6. Gauge-invariant Cartan observables

The node vector \(V_i\) is locally gauge variant. Its raw magnetization is not a physical order parameter. The scan must use gauge-invariant quantities:

- coframe Gram spectra and rank;
- shape-matching defect;
- torsion-loop norm;
- Wilson and MM densities;
- based holonomy traces;
- metric and TT correlators;
- gauge-invariant correlation lengths;
- Ward identities after gauge fixing or through manifestly invariant operators.

A conventional gauge-Higgs order parameter can also obscure analytic continuity between regimes. A new critical surface must be demonstrated through gauge-invariant thermodynamic and correlation observables, not through apparent alignment of \(V_i\).

---

## 7. Conditional weak-mixing diagnostic

The published finite-volume shift exponent for the toroidal \(B-C_b\) transition is approximately

\[
\nu_{\rm vol}=2.7\pm0.4,
\]

with a compatible spherical result near \(2.51\).

Conditionally assuming four-dimensional linear size

\[
N_4\sim L^4,
\]

this corresponds to

\[
\nu_{\rm corr}=\nu_{\rm vol}/4.
\]

If the weakly coupled Cartan sector were in an ordinary Gaussian four-dimensional universality class with \(\nu_C=1/2\), the energy-energy mixing eigenvalue would be

\[
y_{\rm mix}
=\frac1{\nu_{\rm corr}}+\frac1{\nu_C}-4
=\frac4{\nu_{\rm vol}}-2.
\]

The audit gives

| Input | \(\nu_{\rm corr}\) | \(y_{\rm mix}\) |
|---|---:|---:|
| Toroidal central | 0.6750 | −0.5185 |
| Toroidal low | 0.5750 | −0.2609 |
| Toroidal high | 0.7750 | −0.7097 |
| Spherical | 0.6275 | −0.4064 |

Under these assumptions, weak Cartan-CDT mixing is irrelevant: the flow favors a product or spectator fixed point rather than a new mixed RLU fixed point. This is only a diagnostic. The interacting gauge-Cartan sector need not be Gaussian, and strong coupling or a multicritical endpoint can evade it.

---

## 8. The pure-CDT criticality trilemma

The currently known phase structure leaves no already-established trajectory satisfying all three requirements:

\[
\text{continuous transition}
+\text{extended }4D\text{ geometry}
+\text{direct two-helicity spectrum}.
\]

- \(C_{\rm dS}-A\): the established phase diagram classifies it as likely first order, although newer scale-factor renormalization studies report UV-like scaling toward this region and emphasize that the evidence is not yet proof.
- \(C_{\rm dS}-C_b\): likely continuous or higher order, but the neighboring bifurcation phase is not itself the desired smooth de Sitter geometry and the two-helicity spectrum has not been measured.
- \(C_b-B\): higher-order evidence exists, including topology-independent finite-size exponents, but neither side by itself supplies the desired semiclassical de Sitter phase.

The Cartan sector could, in principle, terminate a first-order surface at a critical endpoint or create a new multicritical line that remains on the \(C_{\rm dS}\) side. That is now the most interesting hypothesis.

---

## 9. Production helicity observable

Use toroidal spatial topology and harmonic scalar coordinates \(\phi^a(x)\). On each spatial slice, infer a local spatial metric from the intrinsic Cartan coframes and coordinate differences by weighted least squares. Define

\[
\widetilde h_{ij}(\mathbf k,t)
=\sum_xw_xe^{-i\mathbf k\cdot\boldsymbol\phi(x)}
\left[g_{ij}(x,t)-\bar g_{ij}(t)\right].
\]

Project it into TT, vector, transverse-scalar, and longitudinal-scalar channels.

For each channel \(X\), measure

\[
C_X(\mathbf k,\Delta t)
=\left\langle
h_X(\mathbf k,t+\Delta t)h_X(-\mathbf k,t)
\right\rangle.
\]

The TT inverse correlator should be fitted to

\[
\Gamma_{\rm TT}(\omega,\mathbf k)
=m_T^2
+Z_t\widehat\omega^2
+Z_s\widehat k^2
+\alpha_4\widehat k^4
+\cdots.
\]

The two-helicity conditions are

\[
m_TL\to0,
\qquad
Z_t>0,
\qquad
Z_s>0,
\qquad
c_T^2=Z_s/Z_t\to1,
\]

\[
\frac{\alpha_4}{Z_T\xi^2}\to0,
\]

and exactly two positive-residue TT eigenchannels. Every non-TT channel must either remain gapped in units of \(\xi^{-1}\) or have residue tending to zero.

The synthetic end-to-end observable test used two light TT channels and four heavy non-TT channels. It recovered:

| Channel | Input energy | Fitted energy |
|---|---:|---:|
| Plus | 0.23 | 0.2171 |
| Cross | 0.23 | 0.2227 |
| Vector 1 | 0.92 | 0.9273 |
| Vector 2 | 0.92 | 0.7849 |
| Transverse scalar | 1.18 | 1.0681 |
| Longitudinal scalar | 1.42 | 1.6150 |

The TT covariance eigenvalues were

\[
2.19551,
\qquad
2.20316.
\]

The classifier found exactly two light TT channels and zero light non-TT channels. This validates the estimator on controlled data. It is not a measurement from a Cartan-CDT ensemble.

---

## 10. Fixed-complex pilot

A small periodic fixed-complex MM-only control was run with hot and cold starts. At the tested small sizes, large branch separations persisted:

| Size | Maximum hot/cold MM separation | Location |
|---:|---:|---:|
| 16 | 7.72894 | \(\beta=2\) |
| 32 | 7.25165 | \(\beta=2\) |

A longer size-16 run at \(\beta=2\) still gave different late branch means. This is a metastability and algorithm-calibration warning, not evidence for a phase transition. The geometry was frozen; no correlation-length or universal finite-size conclusion can be drawn.

The production simulation requires replica exchange or multicanonical sampling, multiple four-volumes, and dynamical triangulation moves.

---

## 11. Revised phase-search strategy

The earlier protocol focused heavily on \(B-C_b\). The correct scan must cover two possibilities.

### Surface A — continuous continuation of \(C_{\rm dS}-C_b\)

Turn on the Cartan locking and MM terms and test whether a critical line remains continuous while its extended-side observables stay four-dimensional and its TT sector flows to two helicities.

### Surface B — Cartan-induced endpoint of \(C_{\rm dS}-A\)

Search whether the enlarged coupling space turns the likely first-order \(C_{\rm dS}-A\) surface into a line ending at a continuous critical endpoint. A successful endpoint must be approached from the extended \(C_{\rm dS}\) side and pass the full helicity tests.

The initial coupling space is

\[
(k_0,\Delta;\kappa,\beta,\gamma_{\rm reg},\lambda_M,\lambda_T),
\]

with four-volume fixed during each simulation. The homogeneous guide

\[
\beta\approx-\gamma/16
\]

is only a starting coordinate, not a predicted critical line.

---

## 12. Simulation sequence

### Calibration 0 — pure CDT

Reproduce the de Sitter volume profile, phase locations, transition orders, autocorrelation times, and topology dependence.

### Calibration 1 — fixed geometry Cartan sector

On saved \(C_{\rm dS}\), \(C_b\), \(B\), and \(A\) configurations, update only \(V_i,G_{ij}\). Verify gauge invariance, shape locking, torsion control, and sampler ergodicity.

### Calibration 2 — metric-locking flow

Measure the relative-metric correlator and determine whether

\[
m_{\rm rel}\xi\to\infty
\]

or the Cartan kinetic residue tends to zero.

### Coupled scan

Alternate causal Pachner moves with compact Cartan updates. Use replica exchange across \((\Delta,\beta,\lambda_M)\), and multicanonical biasing where histogram bimodality appears.

### Finite-size program

At minimum, simulate four-volumes spanning one order of magnitude. Measure Binder cumulants, latent heat, histogram barriers, correlation-length ratios, volume scaling, spectral dimension, relative-metric gap, torsion gap, and helicity correlators.

### Universality program

Repeat with:

- spherical and toroidal spatial topology;
- two curvature discretizations;
- two blocking prescriptions;
- more than one compatibility action;
- at least two aspect ratios.

---

## 13. Exact pass and kill criteria

### Pass

A universal two-helicity trajectory requires all of:

\[
\xi/a\to\infty,
\qquad
D(N)\propto N^{1/4},
\qquad
\lambda_1(N)\propto N^{-1/2},
\qquad
d_s^{\rm IR}\to4,
\]

\[
P(\operatorname{rank}M_i=4)\to1,
\qquad
(q_1,q_2,q_3)\to(1,2,-4),
\]

\[
N_{\rm light,TT}=2,
\qquad
N_{\rm light,nonTT}=0,
\]

\[
Z_t,Z_s>0,
\qquad
c_T^2\to1,
\qquad
\alpha_4/(Z_T\xi^2)\to0,
\]

\[
m_{\rm rel}\xi\to\infty
\quad\text{or}\quad
Z_C/Z_R\to0,
\]

and positive spectral residues after controlled Lorentzian reconstruction.

### Kill

The branch is rejected if any of the following survives continuum extrapolation:

- first-order coexistence without a critical endpoint;
- Gaussian spectator Cartan sector only;
- branched-polymer or crumpled geometry;
- four massless helicities from two independent metrics;
- a finite relative massive-spin-2 pole inside the claimed fundamental spectrum;
- a finite opposite-residue \(k^4\) pole;
- massless scalar, vector, or torsion channels;
- topology- or discretization-dependent continuum exponents;
- lack of reflection positivity or a controlled Lorentzian continuation.

---

## 14. Present verdict

| Statement | Status |
|---|---|
| Pure CDT has an extended four-dimensional de Sitter-like phase | Supported by published simulations |
| Pure CDT has an established UV fixed point | Indicated, not proved |
| Pure CDT has a directly measured two-helicity graviton spectrum | No |
| Existing generic Cartan-CDT action has exactly two helicities | No |
| TT/vector/scalar projectors are defined and numerically exact | Yes |
| Finite physical Wilson coefficient is compatible with strict two-helicity fundamental spectrum | No, unless it decouples or is part of a proved nonlocal/topological completion |
| Independent Cartan and Regge metrics are compatible with two massless helicities | No; they give four |
| A single-metric locking/decoupling surface is mathematically coherent | Yes |
| Production helicity estimator works on synthetic data | Yes |
| A universal Cartan-CDT two-helicity critical trajectory has been observed | No |
| A decisive simulation protocol now exists | Yes |

The strongest honest conclusion is:

\[
\boxed{
\text{Cartan-CDT does not yet demonstrably possess a universal two-helicity trajectory.}
}
\]

The original action is too broad. The only surviving candidate is the codimension-at-least-three surface defined by

\[
\boxed{
\text{continuous }C_{\rm dS}\text{-side criticality},
\quad
m_{\rm rel}\xi\to\infty\text{ or }Z_C\to0,
\quad
m_T\xi\to\infty,
\quad
\alpha_4/(Z_T\xi^2)\to0.
}
\]

This is narrow enough to be tested and killed. It is also broad enough to allow the Cartan sector to act as a microscopic completion rather than an additional low-energy gravitational field.

---

## Reproducibility files

- `rlu_stage21_two_helicity_audit.py`
- `rlu_stage21_linear_curvature_symbolic.py`
- `rlu_stage22_fixed_complex_mm_scan.py`
- `rlu_stage22_long_relaxation.py`
- `rlu_stage23_single_metric_locking.py`
- `rlu_stage24_cdt_helicity_observable.py`
- associated JSON, CSV, and text results under `rlu_stage21_results`, `rlu_stage22_results`, `rlu_stage23_results`, and `rlu_stage24_results`

## Primary literature consulted

- Ambjørn and Loll, *Causal Dynamical Triangulations: New Lattice Theory of Quantum Gravity*, arXiv:2604.05641.
- Ambjørn et al., *Is Lattice Quantum Gravity Asymptotically Safe?*, arXiv:2408.07808.
- Ambjørn et al., *The higher-order phase transition in toroidal CDT*, arXiv:2002.01051.
- Ambjørn et al., *Scalar fields in Causal Dynamical Triangulations*, arXiv:2105.10086.
- Ambjørn et al., *Critical Phenomena in Causal Dynamical Triangulations*, arXiv:1904.05755.

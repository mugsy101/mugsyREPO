# RLU Stages 13–15 — Intrinsic Cartan Calculus and a Working Classical Regulator

## Status

This stage replaces the failed weight-only tensor program with an intrinsic Cartan construction. The resulting finite regulator is mathematically defined, locally gauge covariant, and has the correct classical linear spectrum. It is a **working classical RLU-C regulator**, not yet a proof of a background-free quantum continuum theory or of empirical realization in nature.

## 1. Kernel optimization closes as a secondary route

An eight-layer polynomial kernel was optimized subject to the exact four-dimensional infrared constraints

\[
Q(1/2)=Q(1)=Q(3/2)=0,\qquad Q'(3/2)=-2/3.
\]

The optimized polynomial coefficients were

\[
p=(1.002387,-5.407226,-2.684535,3.412004,0.428445,-0.260877,0.004033,0.001472),
\]

corresponding to discrete layer coefficients

\[
c_j=j!p_j=(1.002387,-5.407226,-5.369070,20.472027,10.282686,-31.305293,2.903550,7.420939).
\]

The constraint residual was below \(1.1\times10^{-14}\). Independent Monte Carlo tests showed that it can match the standard four-layer variance at some effective densities, but it does not uniformly improve the deterministic bias. The five-layer kernel still gives the fastest high-density bias decay, at roughly 20–26 times the variance. No single scalar kernel beat both benchmarks over the tested grid.

**Decision:** generalized layer kernels remain useful diagnostics and control variates, but they are no longer the core microscopic derivative.

## 2. Intrinsic matrix-normalized derivative

Let \(E_i^A\) be Cartan displacements from a base event to a finite local neighborhood, all transported into the base frame. Let \(w_i\) be Lorentz-scalar weights. Define

\[
M^A{}_B=\sum_i w_i E_i^A E_{iB},\qquad
b^A=\sum_i w_iE_i^A[\phi_i-\phi_0],
\]

and solve

\[
M^A{}_B(\mathcal D\phi)^B=b^A.
\]

Under a local Lorentz change at the base,

\[
E_i\mapsto\Lambda E_i,\quad M\mapsto\Lambda M\Lambda^{-1},\quad b\mapsto\Lambda b,
\]

so

\[
\mathcal D\phi\mapsto\Lambda\mathcal D\phi.
\]

### Exact affine theorem

For any affine field

\[
\phi_i-\phi_0=p_AE_i^A,
\]

one has \(b^A=M^A{}_Bp^B\). Whenever \(M\) is invertible,

\[
\boxed{(\mathcal D\phi)^A=p^A}
\]

on every realization—not merely in expectation.

Across 2,000 independent past-diamond samples and five neighborhood sizes, mean affine error was approximately \(4.3\times10^{-16}\); the maximum was \(1.6\times10^{-15}\). The median condition number was about 9.3 and the 99th percentile about 11.9.

For a quadratic correction, the error fell as

\[
\|\mathcal D\phi-p\|\propto h^{0.9995},
\]

where \(h\) is the neighborhood size. A finite Lorentz transformation changed the result covariantly to \(9.8\times10^{-16}\).

## 3. Torsion from the intrinsic derivative

Use the synthetic coframe

\[
e^A{}_C(E)=\delta^A_C+\frac12T^A{}_{BC}E^B+\frac12Q^A{}_{CBD}E^BE^D.
\]

For \(Q=0\), the matrix-normalized derivative reconstructed vector, axial, and generic mixed torsion sectors to machine precision on every realization. For \(Q\neq0\), relative torsion error scaled as

\[
\boxed{\|T_{\rm est}-T\|/\|T\|\propto h}
\]

with fitted exponents between 0.9993 and 1.0001.

## 4. Direct loop-holonomy torsion theorem

For a constant-torsion coframe

\[
e^A{}_{\mu}(x)=\delta^A_\mu+\frac12T^A{}_{B\mu}x^B,
\]

the exact line integral around a triangular loop with edge vectors \(u,v\) is

\[
\Theta^A=\frac12\sum_{B<C}T^A{}_{BC}\,(u^Bv^C-u^Cv^B).
\]

Collecting several loops gives a linear system for the 24 independent torsion components. The audited 24-by-24 transfer matrix differed from the identity by

\[
\boxed{3.66\times10^{-15}}.
\]

Independent local frame transformations changed the recovered closure covariantly with error \(2.14\times10^{-16}\).

For a quadratic coframe jet, loop-estimator error scaled as \(h^{0.9983}\). With fixed closure noise, error scaled approximately as \(h^{-2.069}\), displaying the expected area-denominator penalty.

## 5. The microscopic invariant projection matrix

Form

\[
I_1=T_{ABC}T^{ABC},\qquad I_2=T_{ABC}T^{CBA},\qquad I_3=T_AT^A.
\]

The exact constant-torsion loop map gives

\[
\boxed{M_{\rm micro}^{(T)}=I_{24}}
\]

at linear order. On finite cells with a quadratic coframe jet, a fitted three-invariant map approaches the identity:

| Cell size \(h\) | \(\|M-I_3\|\) | Regression residual | Median TEGR error |
|---:|---:|---:|---:|
| 1 | 0.0825 | 0.2859 | 0.2855 |
| 0.5 | 0.0325 | 0.1525 | 0.1477 |
| 0.25 | 0.0316 | 0.0721 | 0.0656 |
| 0.125 | 0.00774 | 0.0383 | 0.0385 |
| 0.0625 | 0.00416 | 0.0198 | 0.0160 |

All three errors scale approximately linearly with \(h\). In this explicit invariant basis the TEGR coefficients are therefore

\[
\boxed{(q_1,q_2,q_3)=\left(\frac14,\frac12,-1\right)\propto(1,2,-4).}
\]

The earlier ratio \(1:-12:8\) is not supported by this construction.

## 6. Joint Cartan curvature and torsion

Represent a Cartan connection by affine 5-by-5 matrices

\[
\mathcal A_\mu=
\begin{pmatrix}
\omega^A{}_{B\mu}&e^A{}_{\mu}\\
0&0
\end{pmatrix}.
\]

For constant connections, the small-loop holonomy obeys

\[
\frac1{h^2}\log\left(e^{h\mathcal A_u}e^{h\mathcal A_v}e^{-h\mathcal A_u}e^{-h\mathcal A_v}\right)
=[\mathcal A_u,\mathcal A_v]+O(h).
\]

The rotational block is curvature and the translational block is torsion. The measured error exponents were

\[
R:\;h^{0.9980},\qquad T:\;h^{1.0008}.
\]

Gauge covariance errors were below \(5\times10^{-17}\).

## 7. Second-order discrete curvature and action

The ordinary based plaquette has \(O(a)\) curvature error. Averaging the logarithms of opposite plaquettes,

\[
\mathcal F_{\rm sym}(a)=\frac{1}{2a^2}\left[\log C(a)+\log C(-a)\right],
\]

cancels the odd Baker–Campbell–Hausdorff terms. The measured refinement laws were

\[
\boxed{\|\mathcal F_{\rm sym}-F\|\propto a^{1.9995}},
\]

\[
\boxed{|S_{\rm lat}-S_{\rm cont}|\propto a^{1.99999}}.
\]

The discrete MacDowell–Mansouri density

\[
\epsilon^{\mu\nu\rho\sigma}\epsilon_{ABCDE}V^E
\mathcal F_{\mu\nu}^{AB}\mathcal F_{\rho\sigma}^{CD}
\]

was invariant under \(SO(1,4)\) transformations to \(9\times10^{-18}\). A locally transformed plaquette obeyed covariance to \(1.3\times10^{-15}\).

The broken-phase expansion into \(R\wedge R\), \(R\wedge e\wedge e\), and \(e^4\) terms closed with zero numerical residual.

## 8. Lattice spin spectrum

The quadratic TEGR tetrad Hessian was constructed on the lattice derivative symbol

\[
q_\mu(k)=\frac{2}{a}\sin\frac{k_\mu a}{2}.
\]

At non-null momentum:

- Hessian rank: 6;
- kernel dimension: 10;
- gauge rank: 10 = 4 diffeomorphism + 6 Lorentz directions;
- physical kernel quotient: 0.

At null momentum:

- Hessian rank: 4;
- kernel dimension: 12;
- gauge rank: 10;
- physical quotient: **2**.

The plus and cross polarizations solve the null equations exactly. Gauge residuals were zero in the continuum-symbol test and below \(5.4\times10^{-16}\) for the lattice symbol.

Thus the finite regulator carries exactly two massless graviton polarizations at quadratic order.

## 9. Convergence in probability and the double-scaling window

Adding independent field/link noise of scale \(\sigma\) to the matrix-normalized derivative gave

\[
\text{error}\propto h^{-1.0026}N^{-0.5135},
\]

consistent with

\[
\text{error}\sim\frac{\sigma}{h\sqrt N}.
\]

In four dimensions, \(N\sim\rho h^4\), so

\[
\text{noise}\sim\frac{\sigma}{\sqrt\rho\,h^3}.
\]

With \(h\sim\rho^{-\alpha}\), deterministic bias behaves as \(\rho^{-\alpha}\) while noise behaves as \(\rho^{-1/2+3\alpha}\). Both vanish when

\[
\boxed{0<\alpha<\frac16.}
\]

This is an explicit convergence-in-probability window for the local Cartan derivative under the stated independent-noise model.

## 10. Minimal working RLU-C regulator

A finite classical regulator can now be defined with:

1. a finite oriented relational 4-complex;
2. node vectors \(V_i\) and Cartan links \(G_{ij}\in\mathrm{Spin}(1,4)\);
3. coframes \(e_{ij}=P_i(G_{ij}V_j-V_i)\);
4. intrinsic local derivatives obtained from the mixed displacement matrix \(M^A{}_B\);
5. torsion from translational loop closure;
6. curvature from the symmetric-clover logarithm;
7. the discrete MacDowell–Mansouri action or, in the teleparallel sector, the TEGR invariant combination;
8. compact internal gauge links and an overlap/domain-wall matter regulator.

For a Euclidean finite regulator, replacing \(\mathrm{Spin}(1,4)\) by compact \(\mathrm{Spin}(5)\) gives a finite-dimensional compact bosonic integration domain. This establishes a finite mathematical model.

## 11. What is and is not proved

### Established

- intrinsic, locally Lorentz-covariant displacement calculus;
- exact affine derivative on each nondegenerate realization;
- exact constant-torsion recovery;
- a finite-cell \(M_{\rm micro}\) approaching the identity;
- second-order curvature/action convergence;
- exact classical gauge covariance in the audited constructions;
- the TEGR coefficient ray \(1:2:-4\) in the explicit invariant basis;
- two—and only two—massless graviton polarizations at quadratic order;
- a viable bias/noise double-scaling window.

### Still open

- dynamical generation of a four-dimensional manifold-like phase rather than insertion of a 4-complex;
- a nonperturbative quantum critical point with diverging correlation length;
- reflection positivity/unitary Lorentzian continuation of the full measure;
- anomaly-free chiral matter and mirror decoupling on an irregular dynamical complex;
- universality under graph ensembles and blocking rules;
- derivation of a unique nonzero beyond-GR coefficient;
- empirical confirmation.

## Conclusion

The weight-only causal-layer route is no longer needed. The Cartan-link route now supplies a coherent classical microscopic calculus and a finite regulator whose continuum diagnostics reproduce GR/TEGR with the correct spectrum. The decisive remaining claim is no longer “can RLU define gravity?” It can, conditionally on its Cartan link variables. The decisive claim is:

\[
\boxed{\text{Does this finite regulator possess a background-free four-dimensional quantum critical phase?}}
\]

That is the next nonperturbative gate.

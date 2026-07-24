# RLU Stages 16B–19 — Interacting Measure, Graph Entropy, and the Cartan-CDT Frontier

## Status

RLU-C now has a finite compact Euclidean regulator, an intrinsic coframe and curvature construction, the correct free two-helicity limit, and an exact finite five-colored pseudomanifold realization. The present unresolved question is no longer whether a regulator can be written. It is whether the interacting sum over geometries has a non-Gaussian four-dimensional continuum phase.

This report records both progress and exclusions. The strongest new exclusion is that a local regular-simplex frame action is completely blind to melonic global topology. The strongest constructive result is an exact gauge-covariant two-simplex colored regulator and a fully specified Cartan-CDT production theory.

---

# 1. Four dimensions are selected, not generated

With

\[
V_i\in S^4\subset\mathbb R^5,
\qquad P_i=I-V_iV_i^T,
\]

we have

\[
\operatorname{spec}P_i=(1,1,1,1,0),
\qquad \operatorname{rank}P_i=4.
\]

Every intrinsic coframe

\[
e_{ij}=P_i(G_{ij}V_j-V_i)
\]

lies in a four-dimensional tangent image. RLU-C is therefore background-free with respect to geometry, but the local dimensionality is selected algebraically by `SO(5) -> SO(4)`. A separate dimension-neutral extension would be needed to claim that the number four itself emerges.

---

# 2. The finite Euclidean measure exists and is positive

For a finite graph or complex,

\[
G_e\in SO(5),\qquad V_i\in S^4,
\]

so the configuration domain is compact. Any real continuous local action is bounded on this domain and

\[
0<Z_K=\int e^{-S_E}\,d\mu<\infty.
\]

The MacDowell–Mansouri density can have either sign without producing a complex Boltzmann weight. The remaining quantum issues are criticality, reflection positivity, Lorentzian reconstruction and universality rather than a generic bosonic sign problem.

---

# 3. Branch-free curvature

Define

\[
\mathcal A(U)=\frac12(U-U^T)
\]

and average opposite clover orientations,

\[
F_{\rm bf}(a)=
\frac{\mathcal A(H_+(a))+\mathcal A(H_-(a))}{2a^2}.
\]

The numerical refinement slope was

\[
1.9912245,
\]

consistent with second-order convergence. Local gauge covariance held to

\[
7.30\times10^{-15}.
\]

This removes the principal-log branch ambiguity from the finite regulator.

---

# 4. The simple fixed-lattice subsectors do not supply interacting gravity

At zero gauge stiffness, links are independent. For `x=U_55` under Haar `SO(5)`,

\[
p(x)=\frac34(1-x^2),
\]

and

\[
Z_1(\kappa)=
\frac{3(\kappa\cosh\kappa-\sinh\kappa)}{\kappa^3}.
\]

This sector is analytic at finite coupling and contains no critical continuum limit.

At infinite stiffness, the model reduces to a four-dimensional fixed-length `O(5)` model. The pilot transition lies near

\[
\kappa\approx0.77\text{--}0.80.
\]

Because four is the upper critical dimension of the ordinary order-parameter theory, this boundary supplies a Gaussian benchmark with logarithmic corrections, not the desired interacting quantum-gravity fixed point.

Finite-stiffness simulations showed an `O(5)`-like sharpening but no regulator-independent non-Gaussian crossing.

---

# 5. Homogeneous MacDowell–Mansouri phase theorem

For

\[
U_\mu=\exp(\theta J_{\mu5}),\qquad V=e_5,
\]

we obtain

\[
\det e=\sin^4\theta,
\]

\[
W(\theta)=6(\cos^2\theta-4\cos\theta+3)\sin^2\theta,
\]

and

\[
Q(\theta)=24(\sin^4\theta+4\sin^2\theta\cos\theta-4\sin^2\theta+4)\sin^4\theta.
\]

For

\[
V_{\rm hom}=-4\kappa\cos\theta+\gamma W+\beta Q,
\]

the quartic coefficient at `kappa=0` is

\[
u=6\gamma+96\beta.
\]

Hence the exact homogeneous tricritical guide is

\[
\boxed{\beta_{\rm tri}=-\gamma/16}.
\]

The Wilson and MM terms begin at quartic order in the coframe; `kappa` is the independent quadratic mass/cosmological counterterm. The homogeneous continuous branch is still Gaussian, so graph dynamics must generate any nontrivial fixed point.

---

# 6. Why simple graph rewards fail

Equal degree does not determine spectral dimension, and a local square reward selects pathological block graphs more strongly than a four-dimensional torus. Consequently, degree and a finite list of short-cycle counts cannot define four-dimensional locality.

An intrinsic local frame action can enforce rank and conditioning. For outgoing coframes `e_j`, define

\[
M=\sum_j e_je_j^T.
\]

Then

\[
\operatorname{Tr}M\operatorname{Tr}M^{-1}\ge16,
\]

with equality iff `M` is isotropic. Closure and full rank require at least five positive-weight edges; at degree five the zero-defect solution is the regular four-simplex,

\[
\sum_{a=1}^5e_a=0,
\qquad e_a\cdot e_b=-\ell^2/4\quad(a\ne b).
\]

This establishes local nondegeneracy, but Stage 19 shows that it does not control global topology.

---

# 7. Exact finite five-colored regulator

The minimal closed colored complex is a bipartite dipole: two oppositely oriented four-simplices joined by one edge of each of five colors.

For the audited regular-simplex configuration:

- both moment matrices had rank four;
- closure and isotropy errors were approximately `1e-16`;
- opposite orientation required an odd local color permutation;
- the two MM contributions added rather than cancelling;
- the total MM density was
  \[
  -0.3522133651;
  \]
- scalar gauge invariance held to
  \[
  6.22\times10^{-15};
  \]
- coframe and curvature covariance errors were below
  \[
  6\times10^{-16}.
  \]

Therefore an intrinsic, finite, positive and gauge-covariant RLU-C pseudomanifold regulator exists exactly. This is a regulator-existence result, not a continuum result.

---

# 8. Entropy selects branched polymers in the unrestricted colored ensemble

A random melonic five-colored ensemble was sampled up to 512 graph vertices. The finite-size diameter fit gave

\[
d_H^{\rm pilot}\approx2.26,
\]

and the largest-size spectral plateau estimate was

\[
d_s^{\rm pilot}\approx1.408,
\]

close to the branched-polymer value `4/3`. The finite-size estimates should not be mistaken for exact critical exponents, but they agree with the known melonic continuum class.

This gives the first graph-entropy verdict:

\[
\boxed{
\text{the unrestricted colored measure does not generate four-dimensional spacetime.}
}
\]

---

# 9. New local-frame no-go theorem

Let `n_a`, `a=0,...,4`, be the five unit vectors of a regular four-simplex,

\[
\sum_an_a=0,
\qquad n_a\cdot n_b=-1/4\quad(a\ne b).
\]

Choose one color-dependent link matrix `G_a` satisfying

\[
P(G_aV-V)=\sin\theta\,n_a.
\]

On any proper bipartite five-colored graph, assign `G_a` to every black-to-white edge of color `a`. Then every black vertex has frame

\[
e_{v,a}=+\sin\theta\,n_a,
\]

and every white vertex has

\[
e_{v,a}=-\sin\theta\,n_a.
\]

Thus every vertex has exactly zero closure, isotropy and equal-length defect, independent of global graph topology.

The numerical audit covered random melonic graphs from 2 to 1,024 vertices and found:

- maximum closure error `9.45e-17`;
- maximum isotropy error `1.23e-16`;
- maximum length variance `9.24e-34`;
- minimum frame rank `4`.

Therefore

\[
\boxed{
S_{\rm frame}\text{ is necessary for a good local tetrad but cannot suppress melons.}
}
\]

The bicolored face count obeyed the exact melonic identity

\[
\boxed{F=3N+4}.
\]

Each insertion adds two vertices and six faces. At large sampled size, approximately 71% of bicolored faces had minimal length two. The topology problem is extensive and must be addressed by graph/causal or curvature dynamics.

---

# 10. Consequence: RLU splits into two programs

## RLU-C4

Fix local dimension four and sum over causal four-dimensional triangulations. This is the viable near-term program. The leading candidate is Cartan variables on four-dimensional Causal Dynamical Triangulations, whose graph ensemble already avoids the unrestricted melonic entropy problem and has an extended semiclassical phase plus higher-order transition candidates.

## RLU-E

Attempt to make dimensionality itself emergent. This requires a dimension-neutral action and a sum over internal ranks or tensor ranks. The present MM four-form cannot establish this because four is already in the microscopic data. This program remains speculative and separate.

---

# 11. Minimal Cartan-CDT action

On a causal triangulation `K`, use

\[
S=S_{\rm CDT}+S_\kappa+S_{\rm frame}+S_W+S_{\rm MM},
\]

with

\[
S_\kappa=-\kappa\sum_{\langle ij\rangle}V_i\cdot G_{ij}V_j,
\]

an intrinsic rank/closure frame term, a dual-face Wilson term, and the oriented MM cell density. The first search should scan near

\[
\beta\approx-\gamma/16,
\]

while alternating causal triangulation moves with compact Cartan updates.

The graph-only limit must first reproduce known CDT observables. The Cartan fields are then turned on at fixed graphs, followed by the fully coupled scan.

---

# 12. Continuum pass conditions

A surviving trajectory must satisfy simultaneously:

\[
\xi/a\to\infty,
\qquad d_H\to4,
\qquad d_s\to4\text{ in the infrared},
\]

\[
P(\operatorname{rank}M_i=4)\to1,
\]

\[
(q_1,q_2,q_3)\to(1,2,-4),
\]

and a universal massless spin-2 correlator with exactly two positive-residue helicities.

It must survive changes in spatial topology, blocking rule, graph move implementation and regulator details. Reflection positivity or a controlled Lorentzian reconstruction is also mandatory.

The microscopic branch is rejected if the only available limits are analytic crossover, Gaussian `O(5)`, first-order bulk transition, melonic branched polymer, crumpled geometry or a phase with extra physical poles.

---

# 13. Present scientific verdict

| Statement | Status |
|---|---|
| Finite compact RLU-C Euclidean regulator | Established |
| Positive real bosonic measure | Established |
| Branch-free second-order curvature | Demonstrated |
| Exact finite colored pseudomanifold regulator | Established |
| Local rank-four regular-simplex phase | Established |
| Local frame term selects global 4D geometry | Disproved |
| Unrestricted colored entropy gives 4D | Disproved in the melonic leading sector |
| Fixed-lattice gauge-Higgs sector gives interacting gravity | Not demonstrated; limiting critical branch is Gaussian |
| Homogeneous MM tricritical guide | Derived: `beta=-gamma/16` |
| Cartan-CDT interacting critical trajectory | Open and now fully specified |
| Empirical realization of RLU | Not established |

The correct frontier is no longer to invent more effective throat terms. It is to establish—or kill—the Cartan-CDT critical trajectory. Until that succeeds, the throat and beyond-GR sectors remain conditional effective constructions rather than predictions of the microscopic theory.

---

# 14. Stage 20 entropy bracket

The opposite generic colored-graph ensemble was also tested. Construct a proper bipartite five-colored graph by choosing five independent random perfect matchings between the black and white vertex sets.

At total sizes `N=32,...,512`, the measured diameter was well described by

\[
D(N)\approx0.811\log N+2.043,
\]

while the mean combinatorial-Laplacian gap at `N=512` was

\[
\lambda_1=1.031,
\]

close to the infinite random five-regular tree benchmark

\[
5-2\sqrt4=1.
\]

This is an expander/crumpled phase, not a finite-dimensional manifold.

The two entropy endpoints are therefore:

| Colored ensemble | Diameter | Gap | Continuum character |
|---|---|---|---|
| Melonic/tensor-leading | approximately `N^{1/2}` | closes | branched polymer, `d_s=4/3` |
| Uniform perfect matchings | approximately `log N` | order one | expander/crumpled |
| Required RLU-C4 phase | `N^{1/4}` | `N^{-1/2}` | extended four-dimensional geometry |

The bicolored-face statistics also separate the endpoints. Melonic graphs have exactly

\[
F=3N+4
\]

with about 71% minimal two-cycles in the sampled regime. Uniform colored graphs have only order-logarithmic face counts and faces whose typical lengths grow with `N`.

This produces a sharp simulation compass:

\[
\boxed{
D\propto N^{1/4},\qquad
\lambda_1\propto N^{-1/2},\qquad
F\propto N,
}
\]

alongside a spectral-dimension plateau at four. A finite-size model that merely lies numerically between the two endpoints is insufficient; the exponents must stabilize and the correlation length must diverge.

The entropy bracket strengthens the Cartan-CDT decision. Unrestricted colored graphs do not naturally sit near the desired universality class, whereas causal triangulation dynamics is specifically designed to avoid the dominant Euclidean crumpled and branched-polymer pathologies.

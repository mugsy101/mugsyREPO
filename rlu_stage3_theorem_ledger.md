# RLU Stage 3 — Stability, Defect Matter, and Constructive Existence

## Status

This stage audits two proposed advances:

1. the negative torsion coupling at the TEGR/GR point; and
2. fermion states bound to defects in an H-derived relational sector.

The audit establishes several exact theorems and two reproducible finite-lattice
existence results. It also identifies a no-go statement that changes the matter
hypothesis: the full cone of positive Hermitian matrices is contractible, so a
stable topological particle cannot be a defect of an unconstrained positive H
field alone. A nontrivial vacuum manifold must be selected dynamically.

The results prove existence of a finite regulated RLU-type model and of
localized defect modes inside that model. They do not yet prove a quantum
continuum limit, the Standard Model spectrum, or empirical realization.

---

## Theorem 1 — Exact TEGR irreducible decomposition

Use signature `(-,+,+,+)` and a torsion tensor

\[
T^\rho{}_{\mu\nu}=-T^\rho{}_{\nu\mu}.
\]

Define

\[
v_\mu=T^\nu{}_{\nu\mu},
\qquad
a_\mu=\frac16\epsilon_{\mu\nu\rho\sigma}T^{\nu\rho\sigma},
\]

and the Hayashi–Shirafuji pure tensor

\[
t_{\mu\nu\rho}
=T_{(\mu\nu)\rho}
+\frac13\left(
T^\sigma{}_{\sigma(\mu}g_{\nu)\rho}
-T^\sigma{}_{\sigma\rho}g_{\mu\nu}
\right).
\]

The parity-even quadratic contractions satisfy

\[
I_1=T_{\rho\mu\nu}T^{\rho\mu\nu}
=\frac43t^2-6a^2+\frac23v^2,
\]

\[
I_2=T_{\rho\mu\nu}T^{\nu\mu\rho}
=\frac23t^2+6a^2+\frac13v^2.
\]

The TEGR scalar is

\[
T_{\rm TEGR}=\frac14I_1+\frac12I_2-v^2,
\]

therefore

\[
\boxed{
T_{\rm TEGR}
=\frac23t^2+\frac32a^2-\frac23v^2.
}
\]

If the reconstructed irreducible torsion pieces are

\[
P^\mu{}_{\nu\rho}=\frac43t^\mu{}_{[\nu\rho]},
\qquad
A_{\mu\nu\rho}=\epsilon_{\mu\nu\rho\sigma}a^\sigma,
\]

then

\[
P^2=\frac43t^2,
\qquad
A^2=-6a^2,
\]

and the same scalar is

\[
\boxed{
T_{\rm TEGR}
=\frac12P^2-\frac14A^2-\frac23v^2.
}
\]

This validates the proposed coefficients only after the normalization of
"tensor squared", "axial squared", and "vector squared" is stated. In the
canonical scalar basis `(t^2,a^2,v^2)` the coefficients are

\[
\left(\frac23,\frac32,-\frac23\right),
\]

not `(1/2,-1/4,-2/3)`.

### Numerical audit

One hundred random Lorentzian torsion tensors gave

- maximum reconstruction error: `5.274e-16`;
- maximum TEGR/irrep identity error: `7.105e-15`;
- maximum reconstructed-piece identity error: `1.066e-14`.

These are floating-point roundoff levels.

---

## Corollary 1 — The conformal tetrad lies entirely in vector torsion

For

\[
e^a{}_\mu=e^\sigma\delta^a{}_\mu,
\]

one obtains, up to the chosen torsion sign convention,

\[
v_\mu=-3\partial_\mu\sigma,
\qquad
a_\mu=0,
\qquad
t_{\mu\nu\rho}=0.
\]

Hence

\[
\boxed{
T_{\rm TEGR}=-6\,\partial_\mu\sigma\partial^\mu\sigma.
}
\]

The negative vector coefficient is therefore the teleparallel representative
of the conformal direction of GR. It is not an additional propagating
Lorentzian ghost at the TEGR point: the complete constraint algebra leaves the
two GR graviton polarizations.

It does not, by itself, solve the Euclidean conformal-factor problem. A contour
rotation is a candidate definition of the integral. A full nonperturbative
construction must specify the integration cycle, gauge fixing, determinant,
and continuation back to a unitary Lorentzian theory.

---

## Theorem 2 — Finite chiral index and defect pairing

Let a finite Hermitian Hamiltonian obey

\[
\{H,\Gamma\}=0,
\qquad
\Gamma^2=1.
\]

Every nonzero eigenstate at energy `E` is paired with `Gamma|E>` at energy
`-E`, and the two states make cancelling contributions to `Tr Gamma`.
Consequently,

\[
\boxed{
n_+^{(0)}-n_-^{(0)}=\operatorname{Tr}\Gamma.
}
\]

For a finite bipartite lattice with equal global chiral dimensions,

\[
\operatorname{Tr}\Gamma=0.
\]

Therefore one positive-chirality core zero mode requires a negative-chirality
partner at a boundary, an antivortex, or another defect. A locally unpaired
mode is possible; a globally unpaired mode is not possible under these finite
assumptions.

---

## Proposition 2A — One-dimensional H-dimerization defects bind fermions

For a bipartite hopping Hamiltonian

\[
H=\begin{pmatrix}0&Q\\Q^\dagger&0\end{pmatrix},
\]

a change between the two dimerized phases produces a domain wall. In an
infinite or semi-infinite system, the number of protected zero modes is the
change of the bulk winding number. On a finite periodic system, a kink and an
antikink have zero total index and their modes hybridize with exponentially
small splitting.

### Reproducible calculation

For 200 sites with hopping ratio `0.35:1`:

- uniform full gap: `1.300000`;
- clean defect energies: `+5.252e-16`, `-1.559e-15`;
- participation: `1.596` and `2.571` sites;
- centers: bonds/sites near `150` and `50`;
- after 30% off-diagonal disorder and arbitrary link phases: energies remained
  within `8.822e-16` of zero;
- chiral-breaking onsite disorder shifted them to `-2.001e-02` and
  `-5.796e-02`.

The measured splitting law was

\[
\log |E_{\rm split}| = -0.524944\,L+\text{constant},
\]

while the analytic transfer-amplitude prediction is

\[
\frac12\log(0.35)=-0.524911.
\]

### Interpretation

This validates defect binding and chiral-symmetry protection. It does not make
the pair's exact zero energy a global topological theorem. Moreover, all link
phases on an open one-dimensional chain are removable by local basis changes;
a ring retains only its total holonomy. Random phases in 1D mostly test gauge
covariance, not arbitrary physical gauge curvature.

---

## Proposition 2B — A two-dimensional vortex binds one local chiral mode

A four-component lattice Dirac Hamiltonian was coupled to a complex mass
texture

\[
\Delta(\mathbf r)=\Delta_0\tanh(r/\xi)e^{i\theta}.
\]

A naive discretization gave four near-zero modes, the expected species
multiplicity. Adding a Wilson-like flavor-selecting term produced a
one-species topological window while preserving the audit's exact bipartite
chiral operator.

For a `21 x 21` lattice:

- near-zero energies: `+2.991e-08` and `-2.991e-08`;
- resolved bulk gap: `0.424737`;
- core mode: chirality `+1`, mean radius `1.509`, core probability `0.928872`;
- boundary partner: chirality `-1`, mean radius `10.251`, boundary probability
  `0.999994`;
- exact chiral anticommutator norm: numerical zero;
- local gauge covariance error: `1.336e-14`;
- with 30% mass disorder and genuine random plaquette flux, the pair remained
  near zero at `+/-3.284e-06`, with bulk gap `0.433955`.

Thus the vortex creates one **local** chiral core state, while the finite-lattice
index theorem places the opposite chirality at the boundary. This is the right
seed for a domain-wall/vortex construction, but not yet a four-dimensional
anomaly-free chiral spectrum.

---

## Theorem 3 — The unconstrained positive H-sector has no topological defects

Let

\[
\operatorname{Herm}^+(N)
=\{H=H^\dagger\mid H>0\}.
\]

For every `H` and `s in [0,1]`,

\[
F_s(H)=(1-s)H+s\mathbf 1
\]

remains positive definite. Therefore `F_s` is a contraction of the entire
space to the identity. Hence

\[
\boxed{
\pi_k\big(\operatorname{Herm}^+(N)\big)=0
\quad\text{for every }k.
}
\]

Equivalently, `log H` is a global diffeomorphism from the positive cone to the
vector space of Hermitian matrices.

An explicit candidate vortex

\[
H(\theta)=2\mathbf1+
\cos\theta\,\sigma_x+
\sin\theta\,\sigma_y
\]

unwinds continuously by shrinking the Pauli-vector amplitude to zero while
its smallest eigenvalue remains `1`. Therefore positivity never closes the
gap and the winding is not topological in the full H-space.

### Required correction to the matter hypothesis

Replace

> matter is a defect of generic positive H

with

> matter is a defect of an H-derived order parameter whose dynamics selects a
> noncontractible vacuum manifold.

Examples include

- a `Z_2` dimerization manifold in one dimension, giving `pi_0` kinks;
- an `S^1` or Kekule-like complex bond order in two dimensions, giving `pi_1`
  vortices;
- a fixed-eigenvalue adjoint order with an `S^2` vacuum, giving `pi_2`
  monopoles in three dimensions;
- a gauge-Higgs coset with a nontrivial gauge-invariant defect class.

This is not a cosmetic distinction. The potential and symmetry that select the
vacuum manifold must be derived from the relational action.

---

## Theorem 4 — Exact coupling-basis map

Let

\[
\mathcal L=q_1 I_1+q_2 I_2+q_3v^2.
\]

In the canonical irrep order `(t^2,a^2,v^2)`,

\[
\begin{pmatrix}c_t\\c_a\\c_v\end{pmatrix}
=
\underbrace{
\begin{pmatrix}
4/3&2/3&0\\
-6&6&0\\
2/3&1/3&1
\end{pmatrix}}_{M}
\begin{pmatrix}q_1\\q_2\\q_3\end{pmatrix}.
\]

The determinant is `12`, so the map is invertible. TEGR is

\[
(q_1,q_2,q_3)=\left(\frac14,\frac12,-1\right)
\propto(1,2,-4),
\]

which maps to

\[
(c_t,c_a,c_v)=\left(\frac23,\frac32,-\frac23\right)
\propto(4,9,-4).
\]

In the mixed reconstructed-piece order `(P^2,v^2,A^2)`, it is proportional to

\[
(6,-8,-3).
\]

The proposed ratio

\[
1:-12:8
\]

is therefore not the TEGR ratio in any of these standard bases. If interpreted
as `(q_1,q_2,q_3)`, it maps to

\[
\left(-\frac{20}{3},-78,\frac{14}{3}\right),
\]

which is not proportional to TEGR.

It can still be a valid coordinate representation in a different microscopic
basis, but only after deriving an explicit projection matrix `M_micro` and
showing

\[
\boxed{
M_{\rm micro}
\begin{pmatrix}1\\-12\\8\end{pmatrix}
=\alpha
\begin{pmatrix}2/3\\3/2\\-2/3\end{pmatrix},
\qquad \alpha\ne0.
}
\]

No renormalization-group flow toward `1:-12:8` is interpretable as emergence of
GR before this calculation.

---

## Theorem 5 — Finite regulated RLU existence

A mathematically well-defined finite-volume RLU-type model can be constructed.
Let `K` be a finite oriented complex. Assign

- `G_e in Spin(5)` to gravitational links in the Euclidean regulator;
- `V_i in S^4` to nodes;
- `U_e in G_int`, with compact `G_int`, to internal gauge links;
- an H-derived compact order parameter `Phi_i in M` with a specified vacuum
  manifold;
- a finite set of Grassmann spinors to nodes;
- a finite lattice Dirac/overlap matrix `D[G,U,V,Phi]`.

Let the bosonic action be continuous on the compact configuration space. After
integrating the fermions, the finite partition function is

\[
Z_K=\int dG\,dV\,dU\,d\Phi\;
 e^{-S_B[G,V,U,\Phi]}\det D[G,U,V,\Phi].
\]

A continuous function on a compact domain is bounded, and a finite determinant
is a continuous polynomial in the matrix entries. Therefore

\[
\boxed{|Z_K|<\infty.}
\]

This is a constructive existence theorem for the regulator. It does not prove
positivity of the measure, a continuum limit, reflection positivity, or the
existence of the theory in nature.

For noncompact `GL(2,C)` links, finite-volume convergence instead requires an
explicit confining potential or a specified complex integration cycle. Merely
saying "rotate the conformal direction" is not a complete measure definition.

---

## Unifying RLU-C with the H/U spectral branch

The current program contains two ontologies unless they are explicitly joined:

1. RLU-C geometry uses `Spin(1,4)` or `SO(1,4)` links plus the node normal `V`;
2. the original spectral branch uses `Z=HU` with positive Hermitian `H` and
   unitary `U`.

A consistent completion uses the Cartan decomposition relative to `V`:

\[
G_{ij}=B_{ij}\,\Omega_{ij},
\]

where

\[
B_{ij}\in Spin(1,4)/Spin(1,3)
\]

is the geometric coset/boost component and

\[
\Omega_{ij}\in Spin(1,3)
\]

is local Lorentz transport. The discrete coframe remains

\[
e_{ij}=P_i(G_{ij}V_j-V_i).
\]

The role originally assigned to arbitrary positive `H` should be split:

- geometric strain is carried by the Cartan coset/coframe;
- internal gauge transport is carried by compact unitary links;
- defect matter is carried by a derived bond-order/Higgs variable `Phi`, whose
  vacuum topology is generated by the action.

This prevents an arbitrary positive matrix from being asked simultaneously to
supply Lorentzian geometry, gauge covariance, and nontrivial topology.

---

## What a full existence proof now requires

### Gate E0 — finite regulator

**Passed constructively**, as stated in Theorem 5.

### Gate E1 — critical continuum phase

Find a second-order critical surface with

\[
\xi/a\rightarrow\infty,
\]

and demonstrate regulator-independent long-distance observables. A fixed
four-dimensional sprinkling is insufficient because it inserts the dimension
and causal geometry being claimed as emergent.

### Gate E2 — gravity universality

At the critical surface, establish

- diffeomorphism/local-frame Ward identities;
- a massless spin-2 pole;
- only two physical polarizations;
- flow of the projected torsion couplings to the TEGR ray;
- suppression or constraint of all extra scalar/vector modes.

### Gate E3 — Lorentzian unitarity

Specify the Euclidean/complex integration cycle and demonstrate a reconstruction
with positive physical norm and causal propagation. A negative Euclidean
conformal direction is compatible with GR, but it is not by itself a proof of a
valid quantum measure.

### Gate E4 — chiral matter

Derive, rather than insert,

- the nontrivial vacuum manifold;
- a local chiral core spectrum;
- removal or decoupling of mirror/boundary partners;
- anomaly cancellation;
- `SU(3)xSU(2)xU(1)` representations and hypercharges;
- three generations and their mass structure.

A codimension-two vortex or domain-wall/overlap construction is now the
concrete route. The Stage-3 calculation proves the local binding mechanism but
also proves that global chirality must be balanced by boundaries, inflow, or a
modified lattice chiral relation.

### Gate E5 — empirical existence

Derive at least one numerical relation not adjustable by refitting couplings,
then test it experimentally. Until this gate passes, RLU is a mathematical
candidate rather than an observed law of nature.

---

## Immediate executable program

1. Define the three microscopic graph invariants called `planar`,
   `self-dressed`, and `node-dressed` as explicit index contractions.
2. Expand them to quadratic order around the same condensed background.
3. Gauge-fix and compute the Hessian.
4. Project the Hessian onto tensor, axial, vector, and gauge sectors to obtain
   `M_micro`.
5. Test the proposed `1:-12:8` vector with the boxed projection equation above.
6. Only then implement blocking and beta-function estimation.
7. In parallel, derive a complex H-derived bond order `Phi` from gauge-invariant
   link contractions, show that its vacuum manifold has nonzero `pi_1`, and
   repeat the 2D vortex audit without imposing the mass texture by hand.
8. Promote the successful defect to a domain-wall/overlap construction whose
   four-dimensional spectrum and anomaly polynomial can be computed.

The theory is now falsifiable at every stage: a wrong projection matrix, no
critical point, an extra propagating mode, failed anomaly cancellation, or no
unique prediction terminates the corresponding completion.

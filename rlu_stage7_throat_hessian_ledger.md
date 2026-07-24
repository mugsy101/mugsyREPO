# RLU Stage 7 — Defect-Mediated Throat Hessian and Chronology Gate

## Status

This stage constructs and audits a **finite reduced RLU throat regulator**. It proves conditional stability statements for a specified action and identifies a decisive universality obstruction. It does **not** establish a macroscopic spacetime throat, backward time travel, a regulator-independent continuum limit, or empirical realization of RLU.

The main results are:

1. Two H-derived bond-order defects can activate a stable link amplitude.
2. A heavy graph-local bridge induces the predicted low-energy mouth-to-mouth hopping.
3. The shortcut-edge torsion Hessian is positive after the already-required TEGR conformal contour treatment.
4. A geometric bilocal gluing potential is ghost-free at quadratic order only at the Fierz–Pauli trace tuning.
5. A global relational rank with every edge advancing in rank forbids causal cycles.
6. A phase on one throat edge is gauge; physical rotational directionality requires loop holonomy.
7. A geometric shortcut is universal, whereas a selective H-sector shortcut cannot transport ordinary matter without a transducer.
8. A correlated two-endpoint clock transient follows if, and only if, the throat amplitude couples conformally to clocks.

---

# 1. Minimal pair-sector regulator

Let \(\Phi(H)\) be an H-derived bond-order field whose vacuum manifold is noncontractible. This is necessary because the full positive-Hermitian cone is contractible and therefore cannot itself support stable topological defects.

Take two opposite defects at mouths \(A\) and \(B\), with gauge-invariant core indicators

\[
\mathcal D_A,\mathcal D_B\in\{0,1\}.
\]

Introduce a dormant complex relational edge

\[
Q_{AB}=q\,e^{i\theta}
\]

and endpoint transporters

\[
W_{AB}\in \operatorname{Spin}(1,3),
\qquad
U_{AB}\in G_{\rm int}.
\]

A minimal link-amplitude potential is

\[
\boxed{
V(q;\mathcal D_A,\mathcal D_B)
=
\frac12\left(m_0^2-g\mathcal D_A\mathcal D_B\right)q^2
+\frac{\lambda_q}{4}q^4.
}
\]

With no defect pair,

\[
\mathcal D_A\mathcal D_B=0,
\qquad
q=0,
\qquad
V''(0)=m_0^2>0.
\]

With both defects present, define

\[
\mu^2=g-m_0^2.
\]

If

\[
\mu^2>0,
\]

then

\[
\boxed{
q_0^2=\frac{\mu^2}{\lambda_q},
\qquad
V''(q_0)=2\mu^2>0.
}
\]

The condensation energy is

\[
\boxed{
\Delta E_q=-\frac{\mu^4}{4\lambda_q}.
}
\]

If each defect costs \(E_D\), absence of spontaneous throat proliferation requires

\[
\boxed{
2E_D-\frac{\mu^4}{4\lambda_q}>0.
}
\]

### Numerical benchmark

For

\[
m_0^2=1,
\qquad
g=3,
\qquad\lambda_q=2,
\qquad E_D=1,
\]

we obtain

\[
q_0=1,
\qquad
V''(q_0)=4,
\qquad
\Delta E_q=-0.5,
\qquad
E_{\rm create}=1.5.
\]

The throat state is locally stable, but creating the complete defect pair still costs positive energy.

---

# 2. Two H-sector mouths and the induced nonlocal link

A 200-site periodic bipartite chain was given a kink–antikink dimerization texture. The resulting localized states were

\[
E_A=5.25\times10^{-16},
\qquad
E_B=-1.56\times10^{-15},
\]

with participation lengths

\[
P_A=2.56\ \text{sites},
\qquad
P_B=1.59\ \text{sites}.
\]

Thus the two mouth states are exponentially localized defects rather than extended bulk states.

Introduce one heavy graph-local bridge mode \(b\):

\[
H_b
=
\Delta b^\dagger b
+Gq\left(d_A^\dagger b+d_B^\dagger b+\text{h.c.}\right).
\]

For

\[
\Delta\gg Gq,
\]

Schrieffer–Wolff elimination gives

\[
H_{\rm eff}
=
-\frac{G^2q^2}{\Delta}
\left[
 n_A+n_B+d_A^\dagger d_B+d_B^\dagger d_A
\right]
+O\!\left(\frac{G^4q^4}{\Delta^3}\right).
\]

The common diagonal shift is physically irrelevant, leaving the effective throat hopping

\[
\boxed{
J_{\rm wh}=\frac{G^2q^2}{\Delta}.
}
\]

The ideal transfer time is

\[
\boxed{
t_*=\frac{\pi\hbar}{2J_{\rm wh}}.
}
\]

### Exact finite-system result

For

\[
G=1,
\qquad
q_0=1,
\qquad
\Delta=10,
\]

we predict

\[
J_{\rm wh}=0.1,
\qquad
t_*=15.70796.
\]

Exact diagonalization gave

\[
\Delta E_{\rm exact}=0.192425,
\]

versus the predicted bright–dark splitting

\[
2J_{\rm wh}=0.2,
\]

an error of only

\[
3.79\%.
\]

Direct time evolution gave

\[
\boxed{
P_{A\to B}^{\max}=0.974618
}
\]

at

\[
t=16.0939,
\]

while the maximum occupation of the heavy bridge was only

\[
P_b^{\max}=0.03687.
\]

When the link amplitude was switched off,

\[
q=0,
\]

the maximum transfer probability over the same interval fell to

\[
1.8\times10^{-29}.
\]

When the dimerization defects were removed, the uniform chain restored a clean half-gap

\[
\Delta_{\rm half}=0.65.
\]

This is a concrete reduced existence proof for a **defect-to-defect quantum channel**. It is not yet a spacetime throat.

---

# 3. Torsion/nonlocal graph Hessian

Let \(L_0\) be the local graph Laplacian and add one shortcut edge between \(A\) and \(B\):

\[
L(q)
=
L_0+\kappa q^2
(e_A-e_B)(e_A-e_B)^T.
\]

For

\[
\kappa q^2\ge0,
\]

the rank-one update is positive semidefinite.

At the TEGR point, the irreducible torsion coefficients are

\[
(c_t,c_a,c_v)
=
\left(\frac23,\frac32,-\frac23\right).
\]

The representative quadratic graph Hessian is

\[
\mathbb H_T
=
\operatorname{diag}
\left(
\frac23,\frac32,-\frac23
\right)
\otimes L(q).
\]

The negative vector coefficient is the already-identified conformal direction. In the Euclidean regulator, rotate that direction onto its convergent contour:

\[
v\rightarrow i v_E.
\]

Then

\[
\boxed{
\mathbb H_{T,E}
=
\operatorname{diag}
\left(
\frac23,\frac32,\frac23
\right)
\otimes L(q)
\succeq0.
}
\]

### Numerical audit

For a 64-node periodic graph with a positive shortcut edge of weight 3:

- the shortcut Laplacian had no negative eigenvalues;
- the raw Lorentzian representative had 63 negative vector/conformal directions;
- after the vector contour rotation, the negative-eigenvalue count was zero;
- three constant zero modes remained, one in each representative irrep sector;
- the smallest positive rotated eigenvalue was

\[
6.42036\times10^{-3}.
\]

The new edge does not create a new gradient instability. It also does not solve the Euclidean conformal-factor problem; it inherits the same contour requirement as TEGR/GR.

---

# 4. Bilocal coframe gluing and the Fierz–Pauli theorem

A genuine geometric throat needs a relational pullback from the \(B\) mouth to the \(A\) mouth. Let

\[
X_{AB}:N_A\to N_B
\]

be the relational map and let \(W_{AB}\) transport Lorentz indices. The pulled-back coframe is

\[
\bar e^a{}_{\mu,B}(A)
=
W^a{}_b
\,e^b{}_{\nu,B}(X_{AB})
\frac{\partial X_{AB}^{\nu}}{\partial x_A^{\mu}}.
\]

At quadratic order, define the relative metric perturbation

\[
r_{\mu\nu}=h^A_{\mu\nu}-\bar h^B_{\mu\nu}.
\]

The most general Lorentz-invariant quadratic nonderivative gluing term is

\[
\mathcal L_{\rm glue}^{(2)}
=-\frac{m_T^2q_0^2}{8}
\left(
 r_{\mu\nu}r^{\mu\nu}
-\beta r^2
\right).
\]

Write

\[
r_{00}=2n,
\qquad
r_{ij}=\frac{s}{3}\delta_{ij}
\]

in the scalar sector. The mass structure is

\[
4(1-\beta)n^2
+4\beta ns
+\left(\frac13-\beta\right)s^2.
\]

The lapse-squared coefficient is

\[
\boxed{4(1-\beta).}
\]

Only

\[
\boxed{\beta=1}
\]

keeps the lapse linear so that it can impose the constraint removing the sixth spin-2 mode.

For \(\beta\ne1\), the extra scalar has the formal mass scale

\[
m_s^2
=
\frac{m_T^2(4\beta-1)}{2(1-\beta)},
\]

but its residue has the wrong sign: it is the linear Boulware–Deser/Fierz–Pauli ghost.

Therefore the unique quadratic geometric throat potential is

\[
\boxed{
\mathcal L_{\rm glue,FP}^{(2)}
=-\frac{m_T^2q_0^2}{8}
\left(r_{\mu\nu}r^{\mu\nu}-r^2\right).
}
\]

A nonlinear completion must preserve the Hamiltonian constraint, which points to a dRGT/Hassan–Rosen square-root interaction rather than an arbitrary bilocal metric potential.

---

# 5. Gauge-fixed reduced fluctuation spectrum

After diagonalizing into endpoint-symmetric and endpoint-antisymmetric sectors, the Euclidean reduced physical Hessian has the form

\[
\boxed{
\mathbb H_E(p)
=
\operatorname{diag}
\left[
 p^2 I_2,
 (p^2+m_T^2)I_5,
 p^2+2\mu^2,
 (p^2+\Delta^2)I_2,
 \mathbb H_{T,E}^{\rm alg}
\right].
}
\]

The sectors are:

- two massless diagonal graviton helicities;
- five healthy relative massive-spin-2 helicities;
- one throat-amplitude radial mode;
- two real components of the heavy bridge;
- algebraic or constrained torsion representatives, with no independent torsion pole in the minimal model.

For the benchmark

\[
p=0.7,
\qquad
m_T^2=0.4,
\qquad
2\mu^2=4,
\qquad
\Delta=10,
\]

the reduced 13-dimensional representative Hessian had

\[
\lambda_{\min}=0.49,
\qquad
\lambda_{\max}=100.49,
\]

and

\[
\boxed{N_{\rm negative}=0.}
\]

This is a quadratic stability result. It is not a proof of nonlinear stability on arbitrary backgrounds.

---

# 6. Causal-rank theorem

Let every event carry a global relational rank \(\tau\). Require every fundamental propagation edge to satisfy

\[
\Delta\tau_e>0.
\]

For a directed cycle \(C\), returning to the same event would require

\[
\sum_{e\in C}\Delta\tau_e=0.
\]

But if every term is positive,

\[
\sum_{e\in C}\Delta\tau_e>0,
\]

a contradiction. Therefore

\[
\boxed{
\Delta\tau_e>0\ \forall e
\quad\Longrightarrow\quad
\text{no directed causal cycle}.
}
\]

A finite event-graph audit found:

- no cycle when both spatial directions across the throat advanced one global time step;
- an explicit cycle immediately after adding one edge with negative \(\Delta\tau\).

The throat can be bidirectional in space while remaining forward-directed in relational time.

---

# 7. The “spinning time cone” test

## 7.1 One link is not a cone

For two mouth states,

\[
H(\theta)
=J
\begin{pmatrix}
0&e^{i\theta}\\
e^{-i\theta}&0
\end{pmatrix}.
\]

Its eigenvalues are

\[
E_\pm=\pm J,
\]

independent of \(\theta\). The numerical spectral variation over a full \(2\pi\) phase sweep was

\[
1.39\times10^{-17}.
\]

Thus a static phase on a single edge is pure gauge.

If the phase rotates,

\[
\theta=\Omega\tau,
\]

a co-rotating basis removes the phase and produces an endpoint detuning. The maximum transfer becomes

\[
\boxed{
P_{A\to B}^{\max}
=
\frac{4J^2}{4J^2+\Omega^2}.
}
\]

For

\[
J=0.1,
\qquad
\Omega=0.15,
\]

we obtain

\[
P_{\max}=0.64.
\]

Spinning the single phase suppresses resonant transfer; it does not generate time travel.

## 7.2 A loop has physical rotational holonomy

The first gauge-invariant rotational quantity is a Wilson-loop phase

\[
\Phi_W=\sum_{e\in C}\theta_e.
\]

For a three-mouth ring,

\[
E_n=-2J\cos\left(\frac{2\pi n+\Phi_W}{3}\right),
\qquad n=0,1,2.
\]

At

\[
\Phi_W=\frac\pi2,
\]

the numerical and analytic spectra agreed to

\[
2.78\times10^{-17},
\]

and a nonzero circulating relational current appeared.

This is directionality in an internal relational network, not reversal of causal rank. Every propagation edge can still satisfy \(\Delta\tau>0\).

## 7.3 Spin-2 loop tension

A physical phase loop can safely live in a compact internal or H-sector link network. A loop made from multiple interacting gravitational coframes is much more constrained: generic multi-spin-2 cycles can lose the constraints that remove the Boulware–Deser ghost. Therefore the first viable “spinning” RLU structure is an internal Wilson loop coupled to a tree-like geometric throat—not a circular time coordinate.

---

# 8. The universality/selectivity theorem

There are only two clean possibilities.

## Geometric throat

If the shortcut edge changes the Cartan/coframe adjacency, then the principal kinetic operators of all minimally coupled fields inherit the same adjacency. Photons, gravitons, and ordinary matter can all use the channel.

## H-sector throat

If the shortcut appears only in

\[
H_{\rm eff}^{(H)}
=J_{\rm wh}(d_A^\dagger U_{AB}d_B+\text{h.c.}),
\]

then photons and gravitons do not use it. But neither does ordinary uncharged matter.

The finite two-site audit gives:

| Sector | Selective H link | Geometric universal link |
|---|---:|---:|
| H-defect state | 1 | 1 |
| photon | 0 | 1 |
| graviton | 0 | 1 |
| ordinary matter without transducer | 0 | 1 |

Therefore

\[
\boxed{
\text{selectivity}
\quad\Longleftrightarrow\quad
\text{no direct ordinary-craft transport}.
}
\]

A macroscopic transport claim requires a separate, unitary transducer

\[
\mathcal H_{\rm ordinary}
\longleftrightarrow
\mathcal H_H
\]

that maps all gauge charges, rest energy, entanglement, and quantum statistics into the throat-coupled sector and back.

No such transducer has yet been derived.

---

# 9. Link disappearance after defect annihilation

When either topological core disappears,

\[
\mathcal D_A\mathcal D_B\to0,
\]

the stable minimum returns to

\[
q=0.
\]

For weak damping,

\[
\ddot q+\Gamma\dot q+m_0^2q\simeq0.
\]

Because

\[
J_{\rm wh}\propto q^2,
\]

the channel shuts off quadratically as the throat amplitude decays.

The exact finite defect model verifies both parts:

- setting \(q=0\) reduced transfer below \(2\times10^{-29}\);
- removing the defects restored a bulk half-gap of \(0.65\).

---

# 10. Endpoint clock and gravitational transient

Suppose the throat amplitude has a weak conformal endpoint coupling

\[
g_{\mu\nu}^{\rm clock}
=
\left(1+2\beta_c\frac{q^2}{M_*^2}\right)g_{\mu\nu}.
\]

Then a local clock has

\[
\boxed{
\frac{\delta\nu}{\nu}
\simeq
-\beta_c\frac{q^2}{M_*^2}.
}
\]

Since

\[
J_{\rm wh}=\frac{G^2q^2}{\Delta},
\]

we obtain the RLU pair-channel correlation

\[
\boxed{
J_{\rm wh}
=
-\frac{G^2M_*^2}{\beta_c\Delta}
\frac{\delta\nu}{\nu}.
}
\]

Thus the transfer rate and endpoint clock shift must track the same \(q^2\) profile.

For an illustrative opening profile

\[
q(\tau)
=\frac{q_0}{2}
\left[1+\tanh\left(\frac{\tau}{\tau_o}\right)\right],
\]

with

\[
q_0=1,
\qquad
\tau_o=2,
\qquad
\beta_c/M_*^2=10^{-16},
\]

the final shift is

\[
\frac{\delta\nu}{\nu}\simeq-10^{-16}
\]

at both endpoints, with ideal correlation coefficient 1.

The amplitude \(10^{-16}\) is a benchmark, not an RLU prediction. The theory does predict the **paired waveform and transfer-rate correlation** once the coupling is fixed.

A geometric implementation would additionally produce a local gravimetric or ringdown transient. A purely H-sector implementation need not.

---

# 11. Rotating spacetime-cone scale

A rotating mass produces weak frame dragging with dimensionless scale

\[
\epsilon_{\rm drag}
\sim
\frac{2GJ}{c^3R^2}.
\]

Causality bounds rim angular momentum by roughly

\[
J\lesssim MRc,
\]

so

\[
\epsilon_{\rm drag}
\lesssim
\frac{2GM}{c^2R}
=\frac{r_s}{R}.
\]

For a \(10^4\,\mathrm{kg}\), \(10\,\mathrm m\) craft,

\[
\epsilon_{\rm drag}^{\max}
\simeq1.49\times10^{-24}.
\]

An order-one light-cone tilt at \(R=10\,\mathrm m\) requires approximately

\[
M\sim\frac{c^2R}{2G}
=6.73\times10^{27}\,\mathrm{kg},
\]

or

\[
3.55\ \text{Jupiter masses},
\]

with rest energy

\[
6.05\times10^{44}\,\mathrm J.
\]

Therefore ordinary mechanical rotation of a craft cannot produce a strong directed “time cone.” The mathematical rotating-cylinder and rotating-warp-drive metrics are instead strong-gravity or exotic-stress constructions.

RLU’s causal-rank axiom deliberately excludes a true backward-time cone:

\[
\Delta\tau<0
\]

would immediately permit directed cycles. The viable RLU analogue is a rotating **internal holonomy** that steers transfer while global relational time remains monotonic.

---

# 12. Requested 1–8 completion ledger

| Requested computation | Result |
|---|---|
| 1. Build two H-sector defects | Completed in a 200-site kink–antikink regulator; two machine-zero localized states obtained |
| 2. Derive nonlocal link | Heavy bridge integrated out; \(J_{\rm wh}=G^2q^2/\Delta\) |
| 3. Compute gauge-fixed spectrum | Reduced Hessian positive in benchmark; 2 massless + 5 relative massive spin-2 modes plus healthy link/bridge modes |
| 4. Test ghosts/tachyons/gradients/loops | FP tuning required; positive edge Laplacian stable; global positive rank forbids loops |
| 5. Calculate transfer and creation energy | \(P_{\max}=0.9746\), \(t\approx16.09\), positive creation cost 1.5 in benchmark units |
| 6. Show link disappears | \(q=0\) gives \(<2\times10^{-29}\) transfer; defect removal restores gap |
| 7. Exclude ordinary photons/gravitons | Achievable only for an H-selective link, which also excludes ordinary matter without a transducer |
| 8. Derive endpoint transient | Paired clock waveform proportional to \(q^2\), with transfer-rate/clock-shift correlation |

---

# 13. What is established and what is not

## Established within the specified regulator

- A finite, Hermitian, number-conserving defect-to-defect transfer channel exists.
- Its induced hopping agrees with Schrieffer–Wolff matching.
- The throat amplitude can have a stable defect-activated minimum.
- A positive graph shortcut does not create a new gradient instability.
- Fierz–Pauli tuning is necessary for quadratic geometric gluing.
- A positive global relational rank forbids causal loops.
- A single spinning link phase is gauge; loop holonomy is the first physical rotational observable.
- Selective and universal shortcuts have sharply different observable consequences.

## Still open

- Dynamic formation of the H vacuum manifold and defects from the full RLU action.
- A nonperturbative Hamiltonian proof for a \(q\)-dependent dRGT/Cartan throat.
- A unitary ordinary-matter-to-H-sector transducer.
- Suppression of unwanted throat proliferation in the thermodynamic limit.
- A second-order continuum critical point and universal RG observables.
- A unique empirical prediction not shared by generic bimetric, defect, or hidden-sector models.
- Any evidence that such a channel exists in nature.

## Decisive next theorem

The next theorem is no longer the Hessian. It is the transducer/no-go problem:

\[
\boxed{
\text{Can a local, gauge-invariant, unitary map transfer an arbitrary ordinary-matter state into the defect sector without universal geometric coupling?}
}
\]

If the answer is no, RLU may still provide defect-state communication but not craft transport. If the answer is yes, the map must specify charge conservation, energy accounting, entropy, entanglement fidelity, and reconstruction at the destination.

# RLU Stage 9 — Dynamical-Throat Constraint and Chiral-Carrier Ledger

## Status

This stage addresses the two gates left open by Stages 7–8:

1. whether a throat amplitude that opens and closes can multiply a nonlinear Hassan–Rosen/dRGT interaction without restoring the Boulware–Deser scalar; and
2. whether a genuinely four-dimensional, anomaly-audited chiral carrier and gauge-equivariant ordinary/hidden transducer can be constructed at finite regulator size.

The results are conditional but substantive:

- **Pass, exact in FRW:** a lapse-independent scalar prefactor multiplying the Hassan–Rosen potential leaves the interaction linear in both lapses.
- **Pass, homogeneous constraint benchmark:** a nondegenerate point exists on which the two primary constraints and the secondary constraint vanish, while preservation of the secondary fixes a positive relative lapse.
- **No-go for the minimal double kinetic coupling:** one scalar kinetically coupled to both metrics makes the Hamiltonian nonlinear in the relative lapse.
- **Strong-coupling obstruction:** if the relative spin-2 mass vanishes as \(q^2\), the massive-mode strong-coupling scale vanishes as \(q^{2/3}\). The infrared throat EFT cannot by itself justify exact finite-time closure through \(q=0\).
- **Pass, anomaly arithmetic:** one Standard Model generation is free of the audited local anomalies and has an even number of \(SU(2)\) doublets.
- **Pass, finite 4D chiral regulator:** a four-dimensional overlap operator obeys the Ginsparg–Wilson relation to numerical precision and has index \(-1\) with one chiral zero mode in a unit-flux background.
- **Pass, finite gauge transducer:** identical ordinary and hidden copies of one 16-component generation admit an exact unitary swap commuting with all audited \(SU(3)\), \(SU(2)\), and \(U(1)_Y\) generators.
- **Topology rule:** the geometric spin-2 interaction graph must remain acyclic in the controlled construction. Directional Wilson-loop holonomy belongs to the compact internal/H-sector graph, not to a cyclic spin-2 graph.

These results do **not** establish an arbitrary-background Hamiltonian proof for the complete RLU action, a non-Abelian regulator-independent chiral continuum, dynamical defect generation, macroscopic transport, or empirical existence in nature.

---

# Part I — Scalar-controlled nonlinear throat

## 1. Minimal controlled action

Let \(g_{\mu\nu}\) and \(f_{\mu\nu}\) be the effective metrics associated with two RLU mouths after the local Cartan sectors have condensed. Define

\[
S^\mu{}_{\nu}=\left(\sqrt{g^{-1}f}\right)^\mu{}_{\nu}.
\]

The minimal dynamical-throat action is

\[
\begin{aligned}
S={}&\frac{M_g^2}{2}\int d^4x\sqrt{-g}\,R[g]
+\frac{M_f^2}{2}\int d^4x\sqrt{-f}\,R[f]\\
&-m_*^2M_{\rm eff}^2\int d^4x\sqrt{-g}\,
F(q)\sum_{n=0}^{4}\beta_ne_n(S)\\
&+\int d^4x\sqrt{-g}
\left[-\frac{Z(q)}{2}(\nabla q)^2-V(q)\right]
+S_H+S_{\rm matter}.
\end{aligned}
\]

The restrictions are essential:

1. \(F(q)\) is a scalar function of phase-space variables and does not contain either lapse or shift.
2. The kinetic term of \(q\) couples minimally to **one** metric in the controlled model.
3. The metric interaction remains exactly the elementary-symmetric-polynomial Hassan–Rosen/dRGT potential.
4. The spin-2 interaction graph is a tree.

The first throat ansatz is

\[
F(q)=q^2,
\]

so the relative spin-2 mass behaves as

\[
m_T^2(q)=m_*^2q^2.
\]

The same amplitude also controls the H-sector transfer channel:

\[
J_{\rm wh}(q)=\frac{G^2q^2}{\Delta}.
\]

---

## 2. Exact FRW lapse-linearity theorem

Use spatially flat homogeneous metrics

\[
ds_g^2=-N^2dt^2+a^2d\mathbf x^2,
\qquad
ds_f^2=-L^2dt^2+b^2d\mathbf x^2.
\]

Set

\[
r=\frac ba.
\]

The eigenvalues of \(S=\sqrt{g^{-1}f}\) are

\[
\left(\frac LN,r,r,r\right).
\]

The elementary symmetric polynomials are

\[
e_0=1,
\]

\[
e_1=\frac LN+3r,
\]

\[
e_2=3\frac LN r+3r^2,
\]

\[
e_3=3\frac LN r^2+r^3,
\]

\[
e_4=\frac LN r^3.
\]

Since \(\sqrt{-g}=Na^3\), the interaction density becomes

\[
Na^3F(q)\sum_{n=0}^4\beta_ne_n
=a^3F(q)\left[N A(r)+L B(r)\right],
\]

where

\[
A(r)=\beta_0+3\beta_1r+3\beta_2r^2+\beta_3r^3,
\]

and

\[
B(r)=\beta_1+3\beta_2r+3\beta_3r^2+\beta_4r^3.
\]

Therefore

\[
\boxed{
\frac{\partial^2\mathcal L_{\rm int}}{\partial N^2}
=
\frac{\partial^2\mathcal L_{\rm int}}{\partial L^2}
=
\frac{\partial^2\mathcal L_{\rm int}}{\partial N\partial L}
=0.
}
\]

This is an exact algebraic statement for the homogeneous ansatz. Multiplication by \(F(q)\) does not spoil lapse linearity as long as \(F\) itself is lapse- and shift-independent.

The one-metric scalar kinetic term is likewise linear after the Legendre transform:

\[
\mathcal L_q=\frac{a^3Z(q)}{2N}\dot q^2-Na^3V(q),
\]

\[
p_q=\frac{a^3Z(q)}{N}\dot q,
\]

\[
\mathcal H_q=N\left[\frac{p_q^2}{2a^3Z(q)}+a^3V(q)\right].
\]

Thus the scalar introduces a healthy canonical pair but does not consume the lapse multiplier.

---

## 3. Homogeneous primary and secondary constraints

For the audit, take \(Z=1\) and absorb constant normalizations into \(m^2\). The canonical Hamiltonian has the form

\[
H=N\mathcal C_g+L\mathcal C_f.
\]

The two lapse constraints are

\[
\boxed{
\mathcal C_g
=-\frac{p_a^2}{12M_g^2a}
+\frac{p_q^2}{2a^3}
+m^2a^3q^2A(b/a),
}
\]

and

\[
\boxed{
\mathcal C_f
=-\frac{p_b^2}{12M_f^2b}
+m^2a^3q^2B(b/a).
}
\]

Their Poisson bracket defines the homogeneous secondary constraint candidate

\[
\boxed{
\mathcal S=\{\mathcal C_g,\mathcal C_f\}.
}
\]

Because neither \(\mathcal C_g\) nor \(\mathcal C_f\) contains \(N\) or \(L\), \(\mathcal S\) is lapse-independent.

### Exact nondegenerate benchmark

Choose

\[
a=b=q=M_g=M_f=1,
\qquad
m^2=\frac1{10},
\]

\[
(\beta_0,\beta_1,\beta_2,\beta_3,\beta_4)
=(-1,-1,2,-1,-1),
\]

\[
p_a=p_b=\sqrt{\frac65},
\qquad
p_q=0.
\]

The symbolic calculation gives exactly

\[
\mathcal C_g=0,
\qquad
\mathcal C_f=0,
\qquad
\mathcal S=0.
\]

The next brackets are

\[
\{\mathcal S,\mathcal C_g\}=\frac7{50},
\qquad
\{\mathcal S,\mathcal C_f\}=-\frac3{50}.
\]

Preservation of the secondary constraint requires

\[
\dot{\mathcal S}
=N\{\mathcal S,\mathcal C_g\}
+L\{\mathcal S,\mathcal C_f\}=0,
\]

so

\[
\boxed{
\frac LN=\frac73>0.
}
\]

This point is nondegenerate: the secondary constraint does not vanish identically, and its preservation fixes the relative lapse rather than producing an arbitrary evolution.

### Scope of the result

This calculation proves that the proposed scalar-prefactored structure survives a nontrivial homogeneous Dirac-constraint audit. It is not a substitute for the complete field-theoretic proof with arbitrary shifts, spatial dependence, Cartan torsion, matter, and throat-map variables.

---

## 4. Minimal double-kinetic-coupling no-go

Now let the same scalar velocity couple to both lapse sectors:

\[
\mathcal L_q
=\frac{A}{2N}\dot q^2
+\frac{B}{2L}\dot q^2,
\qquad A,B>0.
\]

The conjugate momentum is

\[
p_q=\left(\frac AN+\frac BL\right)\dot q.
\]

The Hamiltonian is

\[
\boxed{
\mathcal H_q
=\frac{p_q^2NL}{2(AL+BN)}.
}
\]

Its lapse Hessian is

\[
\frac{ABp_q^2}{(AL+BN)^3}
\begin{pmatrix}
-L^2&LN\\
LN&-N^2
\end{pmatrix}.
\]

For nonzero \(A,B,p_q\), this matrix has rank one. In terms of the relative lapse \(x=N/L\),

\[
\boxed{
\frac{d^2\mathcal H_q}{dx^2}
=-\frac{ABp_q^2}{(A+Bx)^3}\ne0.
}
\]

Thus one combination of lapses ceases to be a multiplier. In this minimal canonical implementation, the extra Hassan–Rosen constraint is lost.

The RLU design rule is therefore

\[
\boxed{
q\text{ may set the interaction strength, but its fundamental kinetic term couples to one metric only.}
}
\]

Matter may experience a derived effective geometry only after a separate constraint analysis.

---

## 5. The exact-closure strong-coupling obstruction

For a relative massive spin-2 mode, the standard decoupling-limit scale is

\[
\Lambda_3(q)
=\left(M_{\rm eff}m_T^2(q)\right)^{1/3}.
\]

With

\[
m_T^2(q)=m_*^2q^2,
\]

we obtain

\[
\boxed{
\Lambda_3(q)
=M_{\rm eff}^{1/3}m_*^{2/3}|q|^{2/3}.
}
\]

Therefore

\[
\Lambda_3\rightarrow0
\qquad\text{as}\qquad q\rightarrow0.
\]

For an opening or closing process with characteristic frequency \(\omega\), control of the massive-mode EFT requires

\[
\omega\ll\Lambda_3(q).
\]

This implies

\[
\boxed{
|q|\gg q_{\min}
=\frac{\omega^{3/2}}{\sqrt{M_{\rm eff}}\,m_*}.
}
\]

For the dimensionless benchmark

\[
m_*=0.1,
\qquad
M_{\rm eff}=1000,
\qquad
\omega=0.01,
\]

the threshold is

\[
q_{\min}=3.1623\times10^{-4}.
\]

### Interpretation

This does not prove that the underlying theory is singular at \(q=0\). At zero interaction, two independent diffeomorphism symmetries can re-emerge, and the massive/massless decomposition itself changes. It does prove that the **single low-energy massive-spin-2 expansion cannot be trusted all the way through finite-rate closure**.

At least one of the following is required:

1. **Microscopic closure:** the relational graph description replaces the bimetric EFT before \(q\) reaches the strong-coupling region.
2. **Two-patch description:** an interacting bimetric patch is matched to two decoupled GR/Cartan patches near \(q=0\).
3. **Nonzero geometric floor:** \(m_T^2=m_*^2(q^2+q_c^2)\), while the selective H-sector transfer \(J_{\rm wh}\) still vanishes at \(q=0\).
4. **Asymptotic closure:** \(q\) approaches zero only in infinite relational time.

The third option cleanly separates **geometric constraint protection** from **matter-channel on/off control**.

---

## 6. Spin-2 interaction graph theorem

For a graph with \(V\) vertices, \(E\) edges, and \(C\) connected components, its first cycle rank is

\[
\beta_1=E-V+C.
\]

The audited examples are:

| Geometric mouth graph | \(V\) | \(E\) | \(\beta_1\) | Tree? |
|---|---:|---:|---:|---:|
| Two-mouth edge | 2 | 1 | 0 | Yes |
| Three-mouth chain | 3 | 2 | 0 | Yes |
| Three-mouth ring | 3 | 3 | 1 | No |

The controlled architecture is therefore

\[
\boxed{
\text{spin-2 interaction graph: tree}
}
\]

and

\[
\boxed{
\text{directional Wilson-loop holonomy: compact internal/H-sector graph}.
}
\]

This preserves the Stage-7 result that a single edge phase is gauge and a loop phase is physical, while preventing the physical loop from becoming a cyclic network of interacting spin-2 fields.

---

# Part II — First anomaly-audited four-dimensional carrier

## 7. One Standard Model generation

Write every fermion as a left-handed Weyl field:

| Field | \(SU(3)\) | \(SU(2)\) | \(Y\) | Multiplicity |
|---|---|---|---:|---:|
| \(Q_L\) | \(3\) | \(2\) | \(1/6\) | 6 |
| \(u_R^c\) | \(\bar3\) | \(1\) | \(-2/3\) | 3 |
| \(d_R^c\) | \(\bar3\) | \(1\) | \(1/3\) | 3 |
| \(L_L\) | \(1\) | \(2\) | \(-1/2\) | 2 |
| \(e_R^c\) | \(1\) | \(1\) | \(1\) | 1 |
| \(\nu_R^c\) | \(1\) | \(1\) | \(0\) | 1 |

The neutral right-handed neutrino is not required for the ordinary Standard Model gauge-anomaly cancellations, but it gives a 16-component generation and is useful if a later RLU completion gauges \(B-L\).

### \(SU(3)^3\)

\[
\mathcal A_{333}
=2A(3)-A(\bar3)-A(\bar3)
=2-1-1=0.
\]

### \(SU(3)^2U(1)_Y\)

\[
\mathcal A_{33Y}
=2\left(\frac12\right)\left(\frac16\right)
+\left(\frac12\right)\left(-\frac23\right)
+\left(\frac12\right)\left(\frac13\right)
=0.
\]

### \(SU(2)^2U(1)_Y\)

\[
\mathcal A_{22Y}
=3\left(\frac12\right)\left(\frac16\right)
+\left(\frac12\right)\left(-\frac12\right)
=0.
\]

### \(U(1)_Y^3\)

\[
\begin{aligned}
\mathcal A_{YYY}
={}&6\left(\frac16\right)^3
+3\left(-\frac23\right)^3
+3\left(\frac13\right)^3\\
&+2\left(-\frac12\right)^3
+1^3
=0.
\end{aligned}
\]

### Gravitational–\(U(1)_Y\)

\[
\mathcal A_{\rm grav^2Y}
=6\left(\frac16\right)
+3\left(-\frac23\right)
+3\left(\frac13\right)
+2\left(-\frac12\right)
+1
=0.
\]

### Global \(SU(2)\) condition

There are

\[
3+1=4
\]

left-handed \(SU(2)\) doublets when color copies are counted. The number is even, so the ordinary Witten \(SU(2)\) global anomaly is absent.

As an independent arithmetic check, the genuinely chiral Abelian set

\[
(-9,-5,-1,7,8)
\]

obeys

\[
\sum_iq_i=0,
\qquad
\sum_iq_i^3=0,
\]

and contains no \(q,-q\) vectorlike pair.

---

## 8. Four-dimensional overlap-index audit

Use a four-dimensional periodic lattice with linear size

\[
L=3,
\]

so there are

\[
L^4=81
\]

sites and a four-spinor matrix dimension

\[
4L^4=324.
\]

Let \(D_W\) be the Wilson kernel and

\[
H_W=\gamma_5D_W
\]

its Hermitian form. The overlap operator is

\[
D_{\rm ov}=1+\gamma_5\operatorname{sign}(H_W)
\]

in lattice units.

It should obey the Ginsparg–Wilson relation

\[
\boxed{
\gamma_5D_{\rm ov}+D_{\rm ov}\gamma_5
=D_{\rm ov}\gamma_5D_{\rm ov}.
}
\]

Its index is

\[
\boxed{
\operatorname{Index}D_{\rm ov}
=\operatorname{Tr}\left[\gamma_5\left(1-\frac12D_{\rm ov}\right)\right].
}
\]

The background carries one unit of periodic \(U(1)\) flux through each of the \(12\) and \(34\) planes. Every plaquette in those planes has angle

\[
\frac{2\pi}{L^2}=0.6981317008.
\]

### Numerical result

| Quantity | Result |
|---|---:|
| Wilson-kernel Hermiticity error | 0 |
| Kernel spectral gap | 0.3455097811 |
| Ginsparg–Wilson residual, Frobenius norm | \(7.97\times10^{-13}\) |
| Residual per matrix dimension | \(2.46\times10^{-15}\) |
| Overlap index | \(-1\) |
| Number of zero modes | 1 |
| Smallest singular value | \(8.88\times10^{-16}\) |
| Zero-mode chirality | \(-1\) |
| Zero-mode residual | \(1.24\times10^{-15}\) |

Thus the finite four-dimensional regulator contains one unpaired chiral mode, with the index and chirality tied to the gauge-flux topology rather than to a tuned near-zero eigenvalue.

This is a genuine advance beyond the earlier one- and two-dimensional defect demonstrations. It is still an Abelian background test, not a complete interacting \(SU(3)\times SU(2)\times U(1)\) chiral gauge measure.

---

## 9. Gauge-equivariant ordinary/hidden transducer

Let one ordinary generation and one hidden throat-coupled generation carry **identical** representations. Their one-particle Hilbert space is

\[
\mathcal H_O\oplus\mathcal H_H,
\qquad
\dim\mathcal H_O=\dim\mathcal H_H=16.
\]

For every gauge generator \(T^a\), use

\[
T^a_{\rm doubled}
=\begin{pmatrix}
T^a&0\\
0&T^a
\end{pmatrix}.
\]

Define the transducer Hamiltonian

\[
\boxed{
H_T=gq
\begin{pmatrix}
0&I_{16}\\
I_{16}&0
\end{pmatrix}.
}
\]

Because the two representations are identical,

\[
\boxed{
[H_T,T^a_{\rm doubled}]=0
}
\]

for every \(SU(3)\), \(SU(2)\), and \(U(1)_Y\) generator.

The explicit generator audit found

\[
\max_a\|[H_T,T^a_{SU(3)}]\|=0,
\]

\[
\max_i\|[H_T,T^i_{SU(2)}]\|=0,
\]

\[
\|[H_T,Y]\|=0.
\]

At

\[
t_{\rm swap}=\frac{\pi}{2gq},
\]

an arbitrary ordinary state is mapped to the identical hidden state:

\[
|\psi\rangle_O\oplus0_H
\longrightarrow
0_O\oplus(-i)|\psi\rangle_H.
\]

For

\[
g=0.7,
\qquad q=1,
\]

we obtain

\[
t_{\rm swap}=2.2439947526,
\]

with

\[
\boxed{
\mathcal F=1,
\qquad
P_O^{\rm final}=0,
\qquad
P_H^{\rm final}=1.
}
\]

### Energy gate

For matched ordinary and hidden spectra,

\[
[H_T,H_0]=0.
\]

The computed commutator norm is zero. Shifting every hidden energy by \(0.1\) gives

\[
\|[H_T,H_0]\|=0.39598,
\]

so an exact time-independent swap no longer conserves the uncoupled energy. A drive, battery, or dynamical throat field must carry the mismatch.

This is a complete finite representation-space transducer. It is not yet a local Lorentzian field-theory implementation and does not solve macroscopic decoherence or stress-energy transport.

---

# Part III — Combined RLU architecture

## 10. The controlled layered theory

The least contradictory RLU architecture now has five distinct layers.

### Layer A — local geometry

\[
(G_{ij},V_i)
\]

produce Cartan coframes and the GR infrared limit.

### Layer B — geometric mouth coupling

Two mouth geometries interact through a single Hassan–Rosen edge whose coefficient is \(F(q)\). The geometric interaction graph remains a tree.

### Layer C — internal directional holonomy

The compact internal/H-sector graph may contain loops and a Wilson phase

\[
\Phi_W=\sum_{e\in C}\theta_e.
\]

This sector steers transfer direction without forming a cyclic spin-2 interaction graph or reversing fundamental causal rank.

### Layer D — chiral carriers

Overlap/domain-wall modes localized by H-derived topological order carry anomaly-free gauge representations.

### Layer E — transduction

A gauge intertwiner maps the ordinary representation into its hidden counterpart, the H-sector throat transfers it, and a second intertwiner reconstructs it.

The causal-rank condition remains

\[
\Delta\tau_e>0
\]

for every actual propagation edge.

---

## 11. Correlated opening law

If the same amplitude \(q\) controls the geometric relative mass and the hidden transfer channel,

\[
J_{\rm wh}=\frac{G^2q^2}{\Delta},
\]

\[
m_T^2=m_*^2q^2.
\]

Therefore

\[
\boxed{
\frac{J_{\rm wh}}{m_T^2}
=\frac{G^2}{\Delta m_*^2},
}
\]

independent of \(q\).

This yields a prospective RLU consistency relation:

> the endpoint transfer splitting and the relative spin-2 mass shift must rise and fall in fixed proportion during an opening event.

The ratio is not yet predicted numerically because \(G\), \(\Delta\), and \(m_*\) have not been derived from the microscopic graph action. But once those are matched, the relation is more restrictive than treating geometric and hidden-channel effects as independent.

---

## 12. Degrees of freedom at the controlled low-energy point

For two interacting metrics with the Hassan–Rosen constraints and one healthy scalar, the intended bosonic propagating content is

\[
2\quad\text{massless spin-2 helicities},
\]

\[
5\quad\text{massive relative spin-2 helicities},
\]

\[
1\quad\text{throat-amplitude scalar}.
\]

Thus

\[
\boxed{N_{\rm bosonic}=8}
\]

before H-sector carriers and ordinary matter are counted.

A failure of the secondary constraint would add a ninth bosonic mode—the unwanted Boulware–Deser scalar. The exact FRW and minisuperspace audits find no such mode in the controlled coupling, but the arbitrary-background proof remains mandatory.

---

# Proof ledger

| Statement | Status |
|---|---|
| Scalar-prefactored HR potential is linear in both FRW lapses | **Proved exactly** |
| One-metric scalar kinetic term preserves lapse linearity | **Proved exactly** |
| Nondegenerate homogeneous secondary-constraint point exists | **Constructed exactly** |
| Minimal kinetic coupling of one scalar to both metrics preserves the HR multiplier | **Disproved** |
| Massive-mode EFT remains controlled at finite-rate exact closure through \(q=0\) | **Disproved for \(m_T^2\propto q^2\)** |
| Two-mouth and chain spin-2 graphs are acyclic | **Proved combinatorially** |
| Three-mouth spin-2 ring is in the controlled tree class | **Disproved** |
| One SM generation cancels the audited local anomalies | **Proved algebraically** |
| The ordinary Witten \(SU(2)\) obstruction is absent for one generation | **Passes parity count** |
| A finite 4D overlap operator carries one chiral zero mode | **Demonstrated numerically** |
| Exact finite \(SU(3)\times SU(2)\times U(1)_Y\)-equivariant swap exists between identical copies | **Proved and demonstrated** |
| Full non-Abelian chiral lattice measure for RLU exists | **Open** |
| Dynamical H-order produces the required defects | **Open** |
| Complete RLU throat is ghost-free on arbitrary backgrounds | **Open** |
| Regulator-independent Lorentzian continuum exists | **Open** |
| RLU exists in nature | **Requires empirical prediction and test** |

---

# Decisive Stage-10 calculation

The next calculation is no longer another quadratic Hessian. It is a complete canonical constraint and anomaly-inflow calculation for the combined action.

## Gravity/throat branch

1. ADM-decompose both Cartan-induced metrics with arbitrary spatial dependence.
2. Perform the Hassan–Rosen shift redefinition in the presence of \(F(q)\).
3. Include the canonical pair \((q,p_q)\), the H-sector mouth variables, and the relational map \(X_{AB}\).
4. Construct the full primary-constraint matrix.
5. Derive the field-theoretic secondary constraint.
6. Verify that its preservation fixes a relative lapse/shift combination rather than removing the constraint.
7. Determine whether the constraint survives through the transition to the \(q=0\) symmetry-enhanced patch.
8. Compute the principal symbol on time-dependent mouth backgrounds.

## Chiral branch

1. Replace the Abelian flux test with an anomaly-free \(SU(3)\times SU(2)\times U(1)_Y\) overlap/domain-wall regulator.
2. Derive the fermion measure and its integrability condition.
3. Show explicit anomaly inflow between the defect core and its mirror/boundary sector.
4. Demonstrate that the mirror sector is gapped without breaking the target gauge symmetry.
5. Couple the transducer to the overlap projectors rather than to a bare 16-component vector space.
6. Verify exact gauge Ward identities during a complete open–transfer–close protocol.

## Universal pass condition

RLU advances to a serious quantum candidate only if the same finite theory satisfies simultaneously

\[
\boxed{
N_{\rm spin2}=2+5,
\qquad
N_{\rm BD}=0,
\qquad
\operatorname{Index}D=N_L-N_R,
\qquad
\mathcal A_{\rm gauge}=0,
\qquad
\Delta\tau_e>0.
}
\]

The first new obstruction to watch is not ordinary anomaly cancellation. It is whether the dynamical opening field, the overlap projectors, and the secondary gravitational constraint remain compatible in one local Hamiltonian.

---

## Reproducibility

The accompanying program performs:

- symbolic expansion of all FRW elementary symmetric polynomials;
- exact lapse-Hessian calculation;
- symbolic minisuperspace Poisson brackets;
- the double-kinetic-coupling no-go control;
- strong-coupling closure scaling;
- Standard Model anomaly arithmetic;
- construction and diagonalization of a 324-dimensional four-dimensional overlap operator;
- explicit \(SU(3)\), \(SU(2)\), and \(U(1)_Y\) generator construction;
- exact ordinary/hidden transducer evolution; and
- interaction-graph cycle-rank tests.

### Primary literature used as consistency checks

- Hassan and Rosen, *Confirmation of the Secondary Constraint and Absence of Ghost in Massive Gravity and Bimetric Gravity*, arXiv:1111.2070.
- Huang, Piao, and Zhou, *Mass-Varying Massive Gravity*, arXiv:1206.5678.
- Cusin, Khosravi, and Noller, *On scale-free extensions of massive (bi-)gravity*, arXiv:1608.06643.
- Flinckman and Hassan, *On the Uniqueness of Ghost-Free Multi-Gravity II*, arXiv:2604.07625.
- Lüscher, *Exact chiral symmetry on the lattice and the Ginsparg–Wilson relation*, arXiv:hep-lat/9802011.
- Lüscher, *Abelian chiral gauge theories on the lattice with exact gauge invariance*, arXiv:hep-lat/9811032.
- Fukaya, Onogi, Yamamoto, and Yamamura, *Six-dimensional regularization of chiral gauge theories*, arXiv:1607.06174.

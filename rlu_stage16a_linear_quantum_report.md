# RLU Stage 16A — Linearized Quantum Regulator

## Scope

Stages 13–15 produced a finite classical Cartan/TEGR regulator whose gauge-fixed quadratic spectrum contains exactly two physical massless graviton polarizations. Stage 16A quantizes those two physical modes on a fixed periodic four-dimensional lattice.

This is a **quadratic fixed-background quantum result**. It is not a proof of the interacting, fluctuating-complex, background-free RLU phase.

## 1. Physical Gaussian measure

After removal of the diffeomorphism and local-Lorentz gauge directions, each transverse-traceless helicity has Euclidean lattice kernel

\[
K(k)=\widehat k^2,
\qquad
\widehat k_\mu=2\sin\frac{k_\mu}{2}.
\]

For the two physical helicities,

\[
Z_{\rm phys}
=\prod_{k\ne0}[\widehat k^2]^{-1}.
\]

The single global zero mode is removed in the usual finite-volume definition. Every remaining eigenvalue is positive, so the finite-dimensional Gaussian integral exists.

## 2. Position-space propagator

The periodic propagator is

\[
G_L(x)=\frac1{L^4}\sum_{k\ne0}\frac{e^{ik\cdot x}}{\widehat k^2}.
\]

Axis data were fitted to

\[
G_L(r)=\frac{A_L}{r^{p_L}}+C_L.
\]

| L | fitted exponent \(p_L\) | fitted amplitude \(A_L\) | continuum amplitude \(1/(4\pi^2)\) |
|---:|---:|---:|---:|
| 32 | 2.307619 | 0.0404264 | 0.0253303 |
| 48 | 2.183633 | 0.0348881 | 0.0253303 |
| 64 | 2.104153 | 0.0310987 | 0.0253303 |
| 80 | 2.066226 | 0.0292132 | 0.0253303 |
| 96 | 2.041272 | 0.0278861 | 0.0253303 |

Both the exponent and amplitude approach the four-dimensional massless form

\[
G(r)=\frac1{4\pi^2r^2}.
\]

## 3. Spectral dimension

The exact finite-lattice return probability factorizes:

\[
P_L(s)=
\left[
\frac1L\sum_{n=0}^{L-1}
\exp\left(-4s\sin^2\frac{\pi n}{L}\right)
\right]^4.
\]

Define

\[
d_s(s)=-2\frac{d\log P_L}{d\log s}.
\]

The median value in a window excluding lattice-UV and finite-volume-IR regions was:

| L | median \(d_s\) |
|---:|---:|
| 32 | 4.130066 |
| 48 | 4.082710 |
| 64 | 4.060779 |
| 80 | 4.047737 |
| 96 | 4.039547 |

Thus the physical Gaussian regulator approaches spectral dimension four.

## 4. Positive temporal spectral representation

At fixed nonzero spatial lattice momentum, the exact energy is

\[
E(\mathbf p)=2\,\operatorname{arsinh}
\left(\frac{\widehat{\mathbf p}}2\right).
\]

The periodic temporal correlator is

\[
C_{\mathbf p}(t)=
\frac{\cosh[E(L/2-t_*)]}
{2\sinh E\,\sinh(EL/2)},
\qquad
t_*=\min(t,L-t).
\]

Direct momentum summation agreed with this positive spectral form to relative errors between \(2.9\times10^{-15}\) and \(6.4\times10^{-15}\).

The Osterwalder–Schrader reflection matrices had no eigenvalue below \(-10^{-11}\). Their small negative minima, between \(-1.7\times10^{-15}\) and \(-9.6\times10^{-14}\), are numerical roundoff.

## 5. Continuum dispersion

For the lowest nonzero spatial mode, the relative difference between lattice energy and \(|\mathbf p|\) was:

| L | relative dispersion error |
|---:|---:|
| 32 | \(3.197\times10^{-3}\) |
| 48 | \(1.425\times10^{-3}\) |
| 64 | \(8.022\times10^{-4}\) |
| 80 | \(5.136\times10^{-4}\) |
| 96 | \(3.568\times10^{-4}\) |

The error has the expected quadratic small-momentum behavior.

## 6. Stage-16A theorem ledger

### Established

- The gauge-fixed two-helicity finite lattice theory has a finite Gaussian measure after the global zero mode is removed.
- Its position-space propagator approaches \(1/(4\pi^2r^2)\).
- Its heat-kernel spectral dimension approaches four.
- Its temporal correlator has a positive spectral representation.
- Its low-momentum dispersion approaches \(E=|\mathbf p|\).

### Not established

- An interacting nonperturbative continuum limit.
- A background-free sum over relational complexes.
- Reflection positivity of the full Cartan, torsion, matter, and graph-changing measure.
- A second-order critical surface with a diverging correlation length.
- Universality across graph ensembles.
- Empirical realization in nature.

## Conclusion

The working classical RLU-C regulator now also has the correct **linearized quantum** limit. The remaining foundational gate is no longer the free graviton. It is the existence of an interacting, background-free four-dimensional critical phase of the complete finite regulator.

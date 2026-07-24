#!/usr/bin/env python3
"""RLU Stage 13: intrinsic matrix-normalized derivative and loop torsion audit.

Tests:
1. Lorentz-covariant local derivative from Cartan displacements.
2. Exact sample-by-sample affine recovery.
3. Bias scaling on quadratic fields in compact past diamonds.
4. Exact recovery of constant torsion from linear coframes.
5. Direct torsion recovery from translational loop holonomy.
6. Local gauge covariance of path/loop constructions.
7. Error scaling from higher coframe jets and link noise.
"""
from __future__ import annotations
import json, math, itertools
from pathlib import Path
import numpy as np

OUT=Path('/mnt/data/rlu_stage13_results');OUT.mkdir(exist_ok=True)
ETA=np.diag([-1.,1.,1.,1.])

# ---------- Lorentz utilities ----------
def boost_x(beta:float)->np.ndarray:
    g=1/math.sqrt(1-beta*beta)
    return np.array([[g,-g*beta,0,0],[-g*beta,g,0,0],[0,0,1,0],[0,0,0,1]],float)
def rot_z(th:float)->np.ndarray:
    c,s=math.cos(th),math.sin(th)
    return np.array([[1,0,0,0],[0,c,-s,0],[0,s,c,0],[0,0,0,1]],float)
def random_lorentz(rng)->np.ndarray:
    return rot_z(rng.uniform(-1.2,1.2))@boost_x(rng.uniform(-.65,.65))

# ---------- compact past diamond sampler ----------
def sample_past_diamond(rng,n,T=1.0):
    """Uniform points in I((-T,0), (0,0)); all are in the past of the top."""
    u=rng.random((n,4)); pts=np.empty((n,4))
    left=u[:,0]<.5
    q=np.where(left,2*u[:,0],2*(u[:,0]-.5))
    a=.5*T*q**.25
    t=np.where(left,-T+a,-a)
    rr=a*u[:,1]**(1/3)
    ct=1-2*u[:,2]; st=np.sqrt(np.maximum(0,1-ct*ct)); ang=2*math.pi*u[:,3]
    pts[:,0]=t;pts[:,1]=rr*st*np.cos(ang);pts[:,2]=rr*st*np.sin(ang);pts[:,3]=rr*ct
    return pts

# ---------- intrinsic matrix-normalized derivative ----------
def covariant_derivative(E:np.ndarray, delta_phi:np.ndarray, weights=None):
    """Return contravariant gradient d^A from M^A_B d^B=b^A.

    E rows are Cartan displacements in the base frame. weights must be Lorentz scalars.
    """
    if weights is None: weights=np.ones(len(E))
    Elow=E@ETA
    M=np.einsum('i,ia,ib->ab',weights,E,Elow)
    b=np.einsum('i,ia,i->a',weights,E,delta_phi)
    d=np.linalg.solve(M,b)
    return d,M

def derivative_audit(seed=1301):
    rng=np.random.default_rng(seed)
    affine=[]; quad=[]; cov=[]; cond=[]
    p_cov=np.array([.7,-.2,.35,.1])
    p_up=ETA@p_cov
    H=np.array([[.4,.1,-.05,.02],[.1,-.3,.04,.0],[-.05,.04,.2,.03],[.02,0,.03,-.1]])
    for T in [1.0,.5,.25,.125,.0625]:
        nbar=180
        errs=[]; qerrs=[]; cs=[]
        for rep in range(400):
            n=max(8,rng.poisson(nbar)); E=sample_past_diamond(rng,n,T)
            phi=E@p_cov
            d,M=covariant_derivative(E,phi)
            errs.append(np.linalg.norm(d-p_up))
            phi_q=phi+.5*np.einsum('ia,ab,ib->i',E,H,E)
            dq,_=covariant_derivative(E,phi_q)
            qerrs.append(np.linalg.norm(dq-p_up))
            cs.append(np.linalg.cond(M))
        affine.append({'T':T,'mean_error':float(np.mean(errs)),'max_error':float(np.max(errs))})
        quad.append({'T':T,'mean_error':float(np.mean(qerrs)),'sd_error':float(np.std(qerrs,ddof=1))})
        cond.append({'T':T,'median_condition':float(np.median(cs)),'p99_condition':float(np.quantile(cs,.99))})
    slope=float(np.polyfit(np.log([x['T'] for x in quad]),np.log([x['mean_error'] for x in quad]),1)[0])
    # exact covariance test on one nonlinear sample: transform points and field tensor consistently
    E=sample_past_diamond(rng,250,.35); L=random_lorentz(rng)
    phi=E@p_cov+.5*np.einsum('ia,ab,ib->i',E,H,E)
    d,_=covariant_derivative(E,phi)
    Ep=(L@E.T).T
    Linv=np.linalg.inv(L); p_cov_p=p_cov@Linv; H_p=Linv.T@H@Linv
    phip=Ep@p_cov_p+.5*np.einsum('ia,ab,ib->i',Ep,H_p,Ep)
    dp,_=covariant_derivative(Ep,phip)
    cov_error=float(np.linalg.norm(dp-L@d))
    return {'affine':affine,'quadratic':quad,'quadratic_error_slope_vs_T':slope,
            'conditioning':cond,'lorentz_covariance_error':cov_error}

# ---------- torsion tensors and invariants ----------
EPS=np.zeros((4,4,4,4))
for p in itertools.permutations(range(4)):
    inv=sum(p[i]>p[j] for i in range(4) for j in range(i+1,4));EPS[p]=(-1)**inv

def vector_torsion(v):
    T=np.zeros((4,4,4))
    for A in range(4):
      for B in range(4):
       for C in range(4):T[A,B,C]=((A==B)*v[C]-(A==C)*v[B])/3
    return T

def axial_torsion(a):
    Tl=np.einsum('abcd,d->abc',EPS,a)
    return np.einsum('ad,dbc->abc',ETA,Tl)

def random_torsion(rng,scale=.2):
    T=rng.normal(scale=scale,size=(4,4,4));return .5*(T-T.swapaxes(1,2))

def invariants(T):
    Tl=np.einsum('ad,dbc->abc',ETA,T)
    Tu=np.einsum('ad,be,cf,def->abc',ETA,ETA,ETA,Tl)
    I1=float(np.einsum('abc,abc',Tl,Tu));I2=float(np.einsum('abc,cba',Tl,Tu))
    v=np.einsum('aac->c',T);I3=float(v@ETA@v)
    return np.array([I1,I2,I3,.25*I1+.5*I2-I3])

def coframe_values(E,T,Q=None):
    """e^A_C(E)=delta+.5 T^A_BC E^B + optional quadratic Q^A_CBD E^B E^D/2."""
    n=len(E); out=np.broadcast_to(np.eye(4)[:, :, None],(4,4,n)).copy().transpose(2,0,1)
    out += .5*np.einsum('abc,ib->iac',T,E)
    if Q is not None: out += .5*np.einsum('acbd,ib,id->iac',Q,E,E)
    return out

def torsion_from_local_derivative(E,evals):
    # field differences from base identity
    K=np.zeros((4,4,4)) # A,C,B lower derivative index
    for A in range(4):
      for C in range(4):
        d_up,_=covariant_derivative(E,evals[:,A,C]-(1 if A==C else 0))
        K[A,C]=ETA@d_up
    T=np.empty((4,4,4))
    for A in range(4):
      for B in range(4):
       for C in range(4):T[A,B,C]=K[A,C,B]-K[A,B,C]
    return T

def local_torsion_audit(seed=1441):
    rng=np.random.default_rng(seed)
    sectors={'vector':vector_torsion(np.array([.2,.3,-.1,.25])),
             'axial':axial_torsion(np.array([.1,.2,.15,-.12])),
             'mixed':random_torsion(rng,.12)}
    linear=[]; curved=[]
    Q=rng.normal(scale=.18,size=(4,4,4,4));Q=.5*(Q+Q.swapaxes(2,3))
    for name,T in sectors.items():
      for h in [1,.5,.25,.125,.0625]:
        terr=[];qerr=[]
        for rep in range(250):
            E=sample_past_diamond(rng,max(12,rng.poisson(160)),h)
            Te=torsion_from_local_derivative(E,coframe_values(E,T))
            Tq=torsion_from_local_derivative(E,coframe_values(E,T,Q))
            terr.append(np.linalg.norm(Te-T)/np.linalg.norm(T))
            qerr.append(np.linalg.norm(Tq-T)/np.linalg.norm(T))
        linear.append({'sector':name,'h':h,'mean_relative_error':float(np.mean(terr)),'max_relative_error':float(np.max(terr))})
        curved.append({'sector':name,'h':h,'mean_relative_error':float(np.mean(qerr)),'sd_relative_error':float(np.std(qerr,ddof=1))})
    slopes={}
    for name in sectors:
        rr=[x for x in curved if x['sector']==name]
        slopes[name]=float(np.polyfit(np.log([x['h'] for x in rr]),np.log([x['mean_relative_error'] for x in rr]),1)[0])
    return {'linear_coframe':linear,'quadratic_coframe':curved,'quadratic_error_slopes':slopes,
            'true_invariants':{k:invariants(v).tolist() for k,v in sectors.items()}}

# ---------- exact line integrals and loop torsion ----------
def edge_integral(x,y,T,Q=None):
    d=y-x
    # exact for e_C^A=delta + .5 T^A_BC x^B + .5 Q^A_CBD x^B x^D
    val=d.copy()
    val += .25*np.einsum('abc,b,c->a',T,x+y,d)
    if Q is not None:
        # integral_0^1 .5 Q_CBD (x+s d)^B(x+s d)^D d^C ds
        XX=np.outer(x,x)+.5*(np.outer(x,d)+np.outer(d,x))+(1/3)*np.outer(d,d)
        val += .5*np.einsum('acbd,bd,c->a',Q,XX,d)
    return val

def bivector(u,v):
    return np.array([u[B]*v[C]-u[C]*v[B] for B in range(4) for C in range(B+1,4)])
PAIRS=[(B,C) for B in range(4) for C in range(B+1,4)]

def loop_closure(u,v,T,Q=None):
    z=np.zeros(4)
    return edge_integral(z,u,T,Q)+edge_integral(u,v,T,Q)+edge_integral(v,z,T,Q)

def fit_torsion_from_loops(us,vs,closures):
    # closure = .5 sum_{B<C} T_BC Sigma_BC for our independent-pair convention
    X=np.stack([.5*bivector(u,v) for u,v in zip(us,vs)])
    T=np.zeros((4,4,4))
    for A in range(4):
        q=np.linalg.lstsq(X,closures[:,A],rcond=None)[0]
        for val,(B,C) in zip(q,PAIRS):T[A,B,C]=val;T[A,C,B]=-val
    return T,np.linalg.cond(X)

def loop_audit(seed=1551):
    rng=np.random.default_rng(seed);T=random_torsion(rng,.15)
    exact=[]; curved=[]; noisy=[]
    Q=rng.normal(scale=.1,size=(4,4,4,4));Q=.5*(Q+Q.swapaxes(2,3))
    for h in [1,.5,.25,.125,.0625]:
        m=300;us=rng.normal(size=(m,4))*h;vs=rng.normal(size=(m,4))*h
        C=np.stack([loop_closure(u,v,T) for u,v in zip(us,vs)])
        Te,cond=fit_torsion_from_loops(us,vs,C)
        exact.append({'h':h,'relative_error':float(np.linalg.norm(Te-T)/np.linalg.norm(T)),'design_condition':float(cond)})
        Cq=np.stack([loop_closure(u,v,T,Q) for u,v in zip(us,vs)])
        Tq,_=fit_torsion_from_loops(us,vs,Cq)
        curved.append({'h':h,'relative_error':float(np.linalg.norm(Tq-T)/np.linalg.norm(T))})
        # fixed edge-integral noise scales against shrinking area
        sigma=1e-5
        Cn=C+rng.normal(scale=sigma,size=C.shape)
        Tn,_=fit_torsion_from_loops(us,vs,Cn)
        noisy.append({'h':h,'sigma_edge_closure':sigma,'relative_error':float(np.linalg.norm(Tn-T)/np.linalg.norm(T))})
    curve_slope=float(np.polyfit(np.log([x['h'] for x in curved]),np.log([x['relative_error'] for x in curved]),1)[0])
    noise_slope=float(np.polyfit(np.log([x['h'] for x in noisy]),np.log([x['relative_error'] for x in noisy]),1)[0])

    # local gauge covariance on one triangle with independent node frames
    nodes=[np.zeros(4),rng.normal(size=4)*.2,rng.normal(size=4)*.2]
    frames=[random_lorentz(rng) for _ in range(3)]
    gauges=[random_lorentz(rng) for _ in range(3)]
    def cov_closure(fr):
        total=np.zeros(4)
        for i,j in [(0,1),(1,2),(2,0)]:
            phys=edge_integral(nodes[i],nodes[j],T)
            edge_i=fr[i]@phys
            G0i=fr[0]@np.linalg.inv(fr[i])
            total+=G0i@edge_i
        return total
    c0=cov_closure(frames)
    frames2=[gauges[i]@frames[i] for i in range(3)]
    c1=cov_closure(frames2)
    gauge_error=float(np.linalg.norm(c1-gauges[0]@c0))
    return {'exact_constant_torsion':exact,'quadratic_jet':curved,'fixed_noise':noisy,
            'quadratic_error_slope_vs_h':curve_slope,'noise_error_slope_vs_h':noise_slope,
            'local_gauge_covariance_error':gauge_error,'true_invariants':invariants(T).tolist()}

def main():
    result={'matrix_derivative':derivative_audit(),'local_torsion':local_torsion_audit(),'loop_torsion':loop_audit()}
    (OUT/'stage13_cartan_local_torsion.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()

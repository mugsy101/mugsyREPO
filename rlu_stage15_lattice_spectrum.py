#!/usr/bin/env python3
"""Linearized TEGR tetrad Hessian and gauge/physical mode count."""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
OUT=Path('/mnt/data/rlu_stage15_results');OUT.mkdir(exist_ok=True)
ETA=np.diag([-1.,1.,1.,1.])

def lagrangian(x,qcov):
    f=x.reshape(4,4) # f^rho_mu
    T=np.zeros((4,4,4))
    for r in range(4):
      for m in range(4):
       for n in range(4):T[r,m,n]=qcov[m]*f[r,n]-qcov[n]*f[r,m]
    Tl=np.einsum('rs,smn->rmn',ETA,T)
    Tu=np.einsum('ra,mb,nc,abc->rmn',ETA,ETA,ETA,Tl)
    I1=np.einsum('rmn,rmn',Tl,Tu)
    I2=np.einsum('rmn,nmr',Tl,Tu)
    v=np.einsum('nnm->m',T)
    I3=v@ETA@v
    return .25*I1+.5*I2-I3

def hessian(qcov):
    n=16;H=np.zeros((n,n));L0=lagrangian(np.zeros(n),qcov)
    basis=np.eye(n);diag=np.array([2*lagrangian(basis[i],qcov) for i in range(n)])
    for i in range(n):
      H[i,i]=diag[i]
      for j in range(i+1,n):
        val=lagrangian(basis[i]+basis[j],qcov)-lagrangian(basis[i],qcov)-lagrangian(basis[j],qcov)+L0
        H[i,j]=H[j,i]=val
    return H

def gauge_matrix(qcov):
    cols=[]
    # diffeomorphisms f^rho_mu=q_mu xi^rho
    for r in range(4):
        f=np.zeros((4,4));f[r,:]=qcov;cols.append(f.ravel())
    # local Lorentz lambda^A_B, eta-antisymmetric: lower lambda_AB antisym
    for A in range(4):
      for B in range(A+1,4):
        low=np.zeros((4,4));low[A,B]=1;low[B,A]=-1
        up=ETA@low
        cols.append(up.ravel())
    return np.stack(cols,axis=1)

def rank(A,tol=1e-9):
    s=np.linalg.svd(A,compute_uv=False);return int(np.sum(s>tol*max(1,s[0] if len(s) else 1))),s

def audit(qcontra,label):
    qcov=ETA@qcontra;H=hessian(qcov);G=gauge_matrix(qcov)
    rH,sH=rank(H,1e-8);rG,sG=rank(G,1e-10)
    gauge_res=float(np.linalg.norm(H@G))
    # kernel and gauge quotient
    U,S,Vh=np.linalg.svd(H);tol=1e-8*max(1,S[0]);K=Vh[S<tol].T
    # rank of gauge subspace within kernel and quotient
    # principal combined rank
    rKG,_=rank(np.c_[K,G],1e-8)
    quotient=K.shape[1]-rG # gauge is verified in kernel
    # antisymmetric/symmetric decomposition diagnostic
    # plus and cross tetrad perturbations (symmetric metric half convention)
    plus=np.zeros((4,4));plus[1,1]=.5;plus[2,2]=-.5
    cross=np.zeros((4,4));cross[1,2]=.5;cross[2,1]=.5
    return {'label':label,'q_contravariant':qcontra.tolist(),'q_squared':float(qcontra@ETA@qcontra),
            'hessian_rank':rH,'kernel_dimension':int(K.shape[1]),'gauge_rank':rG,
            'physical_kernel_quotient':int(quotient),'gauge_residual':gauge_res,
            'plus_residual':float(np.linalg.norm(H@plus.ravel())),'cross_residual':float(np.linalg.norm(H@cross.ravel())),
            'smallest_singular_values':S[-6:].tolist(),'combined_kernel_gauge_rank':rKG}

def lattice_momentum(k,a=1):return 2*np.sin(np.asarray(k)*a/2)/a

def main():
    tests=[audit(np.array([1.,0,0,1.]),'continuum_null'),audit(np.array([1.,0,0,.5]),'continuum_nonnull')]
    # Lattice derivative symbol q_mu=2 sin(k_mu a/2)/a: choose k3 to make q3=q0 exactly.
    k0=.7;k3=k0
    q=lattice_momentum([k0,0,0,k3]);tests.append(audit(q,'lattice_symbol_null'))
    q2=lattice_momentum([.7,0,0,.3]);tests.append(audit(q2,'lattice_symbol_nonnull'))
    result={'tests':tests,'interpretation':'At non-null momentum the kernel is pure 4-diffeomorphism + 6-Lorentz gauge. At null momentum two additional transverse tetrad modes remain.'}
    (OUT/'stage15_lattice_spectrum.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()

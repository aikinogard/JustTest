from __future__ import division
import numpy as np
cimport numpy as np

DTYPE = np.float64
ctypedef np.float64_t DTYPE_t

cdef extern from "math.h":  
    double pow(double x,double y)
    double sqrt(double x)
    double exp(double x)

cdef double _norm2(np.ndarray[DTYPE_t, ndim=1] a1, np.ndarray[DTYPE_t, ndim=1] a2):
    cdef unsigned int p = a1.shape[0]
    cdef unsigned int i
    cdef double out = 0
    for i from 0 <= i < p:
        out += pow(a1[i]-a2[i],2)
    return out

def c2loops(np.ndarray[DTYPE_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g):
    cdef unsigned int n = f.shape[0]
    cdef unsigned int m = g.shape[0]
    cdef unsigned int p = g.shape[1]
    cdef unsigned int i,j
    cdef np.ndarray[DTYPE_t, ndim=2] out = np.empty((n,m))

    for i in range(n):
        for j in range(m):
            out[i,j] = exp(-sqrt(_norm2(f[i,:],g[j,:])))
    return out


def c4loops(np.ndarray[DTYPE_t, ndim=2] f, np.ndarray[DTYPE_t, ndim=2] g):
    cdef unsigned int n = f.shape[0]
    cdef unsigned int m = g.shape[0]
    cdef unsigned int p = g.shape[1]
    cdef unsigned int i,j,k,l
    cdef np.ndarray[DTYPE_t, ndim=4] out = np.empty((n,m,p,p))

    for i in range(n):
        for j in range(m):
            for k in range(p):
                for l in range(p):
                    out[i,j,k,l] = exp(-pow(f[i,k]-g[j,l],2))
    return out

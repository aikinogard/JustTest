"""
nt 10 Cython 0.006228 f2py 0.002855
nt 15 Cython 0.009936 f2py 0.007112
nt 20 Cython 0.016054 f2py 0.013060
nt 25 Cython 0.028574 f2py 0.021981
nt 30 Cython 0.037834 f2py 0.033699
nt 35 Cython 0.060576 f2py 0.054184
nt 40 Cython 0.073972 f2py 0.048949
nt 45 Cython 0.089237 f2py 0.077568
nt 50 Cython 0.129476 f2py 0.073205
nt 55 Cython 0.152994 f2py 0.097509
nt 60 Cython 0.193433 f2py 0.112468
nt 65 Cython 0.200992 f2py 0.155681
nt 70 Cython 0.218082 f2py 0.133038
nt 75 Cython 0.257968 f2py 0.135395
nt 80 Cython 0.265433 f2py 0.223432
nt 85 Cython 0.303105 f2py 0.174833
nt 90 Cython 0.376835 f2py 0.225140
nt 95 Cython 0.436014 f2py 0.322916
nt 10 Cython 21.535618 f2py 17.534802
nt 15 Cython 52.370158 f2py 43.101739
nt 20 Cython 96.362024 f2py 124.834801
nt 25 Cython 162.758220 f2py 258.451875
nt 30 Cython 243.814551 f2py 495.573174
nt 35 Cython 343.341812 f2py 731.563985
test result consistency:
	two loops equal: True
	four loops equal: True


test speed for 10 runs:
	test two loops calculations
		Cython 0.0654270648956
		f2py 0.00348997116089
	test four loops calculations
		Cython 4.43180584908
		f2py 3.93526220322
"""

import cloops
import floops
import numpy as np
import timeit
import matplotlib.pyplot as plt

n = np.loadtxt('n.txt')
ntlist = np.arange(10,100,5)
rec_c = np.empty_like(ntlist,dtype=float)
rec_f = np.empty_like(ntlist,dtype=float)
for j,nt in enumerate(ntlist):
	nnt = n[:nt]
	t1 = timeit.Timer(lambda: cloops.c2loops(nnt,nnt))
	rec_c[j] = t1.timeit(number=10)
	t2 = timeit.Timer(lambda: floops.f2loops(nnt,nnt))
	rec_f[j] = t2.timeit(number=10)
	print 'nt %d Cython %f f2py %f'%(nt,rec_c[j],rec_f[j])

plt.figure()
plt.plot(ntlist,rec_c,label='Cython')
plt.plot(ntlist,rec_f,label='f2py')
plt.legend(loc=1)
plt.xlabel('feature size')
plt.ylabel('time for 10 runs')
plt.savefig('2loops.pdf')


ntlist = np.arange(10,40,5)
rec_c = np.empty_like(ntlist,dtype=float)
rec_f = np.empty_like(ntlist,dtype=float)
for j,nt in enumerate(ntlist):
	nnt = n[:nt]
	t1 = timeit.Timer(lambda: cloops.c4loops(nnt,nnt))
	rec_c[j] = t1.timeit(number=10)
	t2 = timeit.Timer(lambda: floops.f4loops(nnt,nnt))
	rec_f[j] = t2.timeit(number=10)
	print 'nt %d Cython %f f2py %f'%(nt,rec_c[j],rec_f[j])

plt.figure()
plt.plot(ntlist,rec_c,label='Cython')
plt.plot(ntlist,rec_f,label='f2py')
plt.legend(loc=1)
plt.xlabel('feature size')
plt.ylabel('time for 10 runs')
plt.savefig('4loops.pdf')


n = np.loadtxt('n.txt')[:50,500:600]

print 'test result consistency:'
print '\ttwo loops equal:',np.allclose(cloops.c2loops(n,n),floops.f2loops(n,n))
print '\tfour loops equal:',np.allclose(cloops.c4loops(n,n),floops.f4loops(n,n))
print '\n'

print 'test speed for 10 runs:'
print '\ttest two loops calculations'
print '\t\tCython',timeit.Timer(lambda: cloops.c2loops(n,n)).timeit(number=10)
print '\t\tf2py',timeit.Timer(lambda: floops.f2loops(n,n)).timeit(number=10)

print '\ttest four loops calculations'
print '\t\tCython',timeit.Timer(lambda: cloops.c4loops(n,n)).timeit(number=10)
print '\t\tf2py',timeit.Timer(lambda: floops.f4loops(n,n)).timeit(number=10)
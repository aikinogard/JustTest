import cloops
import floops
import numpy as np
import timeit
import matplotlib.pyplot as plt

n = np.loadtxt('n.txt')
ntlist = np.arange(100,1201,100)
rec_c = np.empty_like(ntlist,dtype=float)
rec_f = np.empty_like(ntlist,dtype=float)
for j,nt in enumerate(ntlist):
	np = n[:,:nt]
	t1 = timeit.Timer(lambda: cloops.c2loops(np,np))
	rec_c[j] = t1.timeit(number=10)
	t2 = timeit.Timer(lambda: floops.f2loops(np,np))
	rec_f[j] = t2.timeit(number=10)
	print 'nt %d Cython %f f2py %f'%(nt,rec_c[j],rec_f[j])
plt.plot(ntlist,rec_c,label='Cython')
plt.plot(ntlist,rec_f,label='f2py')
plt.legend(loc=1)
plt.xlabel('feature size')
plt.ylabel('time for 10 runs')
plt.savefig('2loops.pdf')


n = np.loadtxt('n.txt')
ntlist = np.arange(100,151,10)
rec_c = np.empty_like(ntlist,dtype=float)
rec_f = np.empty_like(ntlist,dtype=float)
for j,nt in enumerate(ntlist):
	np = n[:,:nt]
	t1 = timeit.Timer(lambda: cloops.c4loops(np,np))
	rec_c[j] = t1.timeit(number=10)
	t2 = timeit.Timer(lambda: floops.f4loops(np,np))
	rec_f[j] = t2.timeit(number=10)
	print 'nt %d Cython %f f2py %f'%(nt,rec_c[j],rec_f[j])
plt.plot(ntlist,rec_c,label='Cython')
plt.plot(ntlist,rec_f,label='f2py')
plt.legend(loc=1)
plt.xlabel('feature size')
plt.ylabel('time for 10 runs')
plt.savefig('4loops.pdf')



n = np.loadtxt('n.txt')[:,500:600]

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
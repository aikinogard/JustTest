import os
os.system('f2py -c -m --fcompiler=gnu95 floops floops.f95')
os.system('cython -a cloops.pyx')
os.system('python setup.py build_ext --inplace')

#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
        
a = Body(-1,name='bob')
b = Body(1,name='jill')
sys = System(bodies=[a, b],name='world')

for i in range(1,5):
    sys.step(0.5)
    print "Step #%d" % i
    print sys


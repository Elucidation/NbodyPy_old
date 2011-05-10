#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
        
a = Body(-1,vy=1,name='bob')
b = Body(1,vy=-1,name='jill')
c = Body(0,1,name='kat')
sys = System(bodies=[a, b],name='world',softenLength=0.5)

print "Start"
print sys

for i in range(1,20):
    sys.step(0.5)
    print "Step #%d" % i
    print sys

print "End"
#print sys


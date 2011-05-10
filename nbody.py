#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
from time import *

a = Body(-1,vy=1,name='bob')
b = Body(1,vy=-1,name='jill')
c = Body(0,1,name='kat')
sys = System(bodies=[a, b],name='world',softenLength=0.5)

print "Start"
print sys

startTime = time()
startEnergy = sys.getTotalEnergy()

for i in range(1,1000):
    #c = time()
    sys.step(0.01)
    #print "Step #%d, Step took %g seconds" % (i,time()-c)
    #print sys

print "End"
print sys
endTime = time()-startTime
print "Total Running time: %g seconds" % endTime
print "Energy difference: %g" % (sys.getTotalEnergy()-startEnergy)
print "\nSystem:"
print sys.detailed()


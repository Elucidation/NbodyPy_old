#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
from time import *

NumSteps = 5
dt = 0.5
errThreshold = 0.00001


a = Body(-1,vy=1,name='bob')
b = Body(1,vy=-1,name='jill')
c = Body(0,1,name='kat')
sys = System(bodies=[a, b],name='world',softenLength=errThreshold)

print "Start"
print sys

startTime = time()
startEnergy = sys.getTotalEnergy()

for i in sys.stepMany(NumSteps,dt):
    print "Step #%g, Time:<%g-%g>" % (i,sys.time-dt,sys.time)
    print sys.short()

print "End"
print sys
endTime = time()-startTime
print "Total Running time: %g seconds" % endTime
print "Energy difference: %g" % (sys.getTotalEnergy()-startEnergy)
print "\nSystem:"
print sys.detailed()


#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
from time import *
from visual import * # Vpython for 2.7 needed

NumSteps = 1000000
dt = 0.001
errThreshold = 0.00001


a = Body(-1,0,0,    0,0.25,0,   name='bob')
b = Body(1,0,0,     0,-0.25,0,  name='jill')
sys = System(bodies=[a, b],name='world',softenLength=errThreshold,G=1)

# Visual
L=1
xaxis = curve(pos=[(0,0,0), (L,0,0)], color=(0.5,0.5,0.5))
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=(0.5,0.5,0.5))
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))

ballA = sphere(radius = 0.2, pos=a.pos,color=color.red,make_trail=True)
ballB = sphere(radius = 0.2, pos=b.pos,color=color.blue,make_trail=True)


print "Start"
print sys

startTime = time()
startEnergy = sys.getTotalEnergy()

c = time()
for i in sys.stepMany(NumSteps,dt):
    #print "Step #%g, Time:<%g-%g>" % (i,sys.time-dt,sys.time)
    #print sys
    
    if (time()-c > 1.0/30): # 30Hz framerate
        #rate(100)
        ballA.pos = sys.bodies[0].pos
        ballB.pos = sys.bodies[1].pos
        c = time()
        
        

print "End"
print sys
endTime = time()-startTime
print "Total Running time: %g seconds" % endTime
print "Energy difference: %g" % (sys.getTotalEnergy()-startEnergy)
print "\nSystem:"
print sys.detailed()


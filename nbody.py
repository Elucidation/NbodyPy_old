
#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from system import *
from time import *
from visual import * # Vpython for 2.7 needed
import random



def pause():
    while True:
        rate(50)
        if scene.kb.keys:
            k = scene.kb.getkey()
            return

NumSteps = 1000000
dt = 0.01
errThreshold = 0.1
N = 30

sys = System(n=N,name='world',softenLength=errThreshold,G=1)

for body in sys.bodies:
    body.visual = sphere(radius = 0.2, \
                         pos=body.pos, \
                         color=randRGB(0.2,0.8),\
                         make_trail=False, \
                         interval=1,\
                         retain=250)

# Visual
L=1
xaxis = curve(pos=[(0,0,0), (L,0,0)], color=(0.5,0.5,0.5))
yaxis = curve(pos=[(0,0,0), (0,L,0)], color=(0.5,0.5,0.5))
zaxis = curve(pos=[(0,0,0), (0,0,L)], color=(0.5,0.5,0.5))


print "Start"
print sys

startTime = time()
startEnergy = sys.getTotalEnergy()

c = time()
for i in sys.stepMany(NumSteps,dt):
    #print "Step #%g, Time:<%g-%g>" % (i,sys.time-dt,sys.time)
    #print sys

    
    if (time()-c > 1.0/60): # 60Hz framerate
        rate(100)

        # KEYBOARD INPUT
        if (scene.kb.keys > 0):
            if scene.kb.getkey()==' ':
                pause()

        
        # UPDATE VISUAL
        for body in sys.bodies:
            body.visual.pos = body.pos - sys.getCenter()
        c = time()

        



        

print "End"
print sys
endTime = time()-startTime
print "Total Running time: %g seconds" % endTime
print "Energy difference: %g" % (sys.getTotalEnergy()-startEnergy)
print "\nSystem:"
print sys.detailed()


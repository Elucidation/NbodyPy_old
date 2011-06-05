#!/usr/bin/python
# Filename: nbody.py

from body import *
from system import *
from parser import *
from time import *
from datetime import timedelta # converts seconds to hh:mm:ss
import random

# Load from configuration file
configFile = "defaultNbodyConfig" # Should be located in same directory


tic = time()
SimulationName, NumSteps, dt, sys = parseNbodySystem(configFile)
print " Time to read file: %g seconds" % (time()-tic)
print "Simulation '%s': Number of Steps: %i, dt: %g, G: %g, errThresh: %g" %(SimulationName, NumSteps,dt, sys.G, sqrt(sys.softenLengthSqrd))
print sys
print "------SYSTEM CREATED------"

print "\nDetailed:"
print sys.detailed()
print "Start"
print sys

startEnergy = sys.getTotalEnergy()

startTime = time()
for i in sys.stepMany(NumSteps,dt):
    print "Step #%g" % i
    print sys        
endTime = time()-startTime
print "End\n"
print "Simulation '%s': Number of Steps: %i, dt: %g, G: %g, errThresh: %g" %(SimulationName, NumSteps,dt, sys.G, sqrt(sys.softenLengthSqrd))
print "Total Real running time: %g seconds" % endTime
print "Total Simulation running time: %g seconds" % sys.time
print "Time ratio: %s simulation seconds per real seconds " % (str(timedelta(seconds=sys.time/endTime)))
print "Steps per second: %s" % (str(NumSteps/endTime))
print "Energy difference: %g" % (sys.getTotalEnergy()-startEnergy)
print "World: "
print sys
print "\nDetailed:"
print sys.detailed()


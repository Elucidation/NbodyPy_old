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
options = parseNbodySystem(configFile)
sys = System(bodies=options['bodies'],\
				 name=options['sysName'],\
				 softenLength=options['errThreshold'],\
				 startTime=options['initTime'],\
				 G=options['G'])

if options['doRand'] == 1:	
	sys.createRandomBodies(options['n'])

SimulationName = options['simName']
NumSteps = options['NumSteps']
dt = options['dt']

print " Time to read file: %g seconds" % (time()-tic)
print " Output file: %s " % options['outputfile']
print "Simulation '%s': Number of Steps: %i, dt: %g, G: %g, errThresh: %g" \
	% (SimulationName, NumSteps,dt, sys.G, sqrt(sys.softenLengthSqrd))
print sys
print "------SYSTEM CREATED------"

print "\nDetailed:"
print sys.detailed()
print "Start"
print sys

startEnergy = sys.getTotalEnergy()

startTime = time()

outfile = open(options['outputfile'],'w')
#outfile.write(str(sys)+'\n')
outfile.write('SIMULATION START\n')
outfile.write('%i\n' % sys.size())
c = time()
debugTimeStep = 5 # seconds
outputStepMult = 10 # 1 = use every step, 2 = every other, 3 = every third...
for i in sys.stepMany(NumSteps,dt):
	 if (time()-c > debugTimeStep):
		 print "Step #%g/%g" % (i,NumSteps)
		 c = time()
		 #print sys	 
	 if (mod(i,outputStepMult)==0):
	 	outfile.write(sys.data()+'\n')
    
outfile.write('SIMULATION END\n')
outfile.close()

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


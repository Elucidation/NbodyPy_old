from body import *
from system import *



def parseNbodySystem(filename):
	
	# Initial conditions
	simName = 'none'
	bodies = []
	sysName = 'none'
	errThreshold = 0
	G = 0
	NumSteps = 0
	dt = 0
	
	print "------LOADING NBODY SYSTEM FROM FILE------"
	print "Loading Nbody Configuration from file '%s'..." % filename
	
	file = open(filename);
	
	print "File opened successfully, loading configuration..."
	
	for line in file:		 
		 line = line.strip()
		 
		 if line == '':
		 	continue
		 elif line[0] == '#':
		 	continue
		 elif line == 'SIMULATION':
		 	mode = 'sim'
		 	print "------SIMULATION------"
		 	print "Loading Simulation data..."
		 	continue
		 elif line == 'WORLD':
		 	mode = 'world'
		 	print "------WORLD------"
		 	print "Loading World data..."
		 	continue
		 elif line == 'BODIES':
		 	mode = 'body'
		 	print "------BODIES------"
		 	print "Loading Body data..."
		 	continue
		 
		 if mode == 'sim':
		 	# Do sim reading stuff
		 	# Possible values:
		 	# name seed numSteps dt G errorThreshold
		 	type,value = line.replace(' ','').split('=')
		 	if type == 'name':
		 		simName = value
		 		print "Simulation name set to %s" % simName
		 	elif type == 'seed':
		 		seed = int(value)
		 		print "Seed set to %i" % seed
		 	elif type == 'numSteps':
		 		NumSteps = int(value)
		 		print "Number of steps to calculate set to %i" % NumSteps
		 	elif type == 'dt':
		 		dt = double(value)
		 		print "Time step set to %g" % dt
		 	elif type == 'G':
		 		G = double(value)
		 		print "Gravitation constant G set to %g" % G
		 	elif type == 'errorThreshold':
		 		errThreshold = double(value)
		 		print "Error threshold set to %g" % errThreshold
		 elif mode == 'world':
		 	# Do world reading stuff
		 	# Possible values:
		 	# name initTime
		 	type,value = line.replace(' ','').split('=')
		 	if type == 'name':
		 		sysName = value
		 		print "System Name set to %s" % sysName
		 	elif type == 'initTime':
		 		initTime = double(value)
		 		print "System Starting Time set to %g" % initTime
		 elif mode == 'body':
		 	# Load Body
		 	a = Body();
		 	a.load(line)
		 	bodies.append(a)
		 	print "Loaded Body " + str(a)
	
	print "------FINISHED READING FROM FILE------"
	file.close()
	sys = System(bodies,name=sysName,softenLength=errThreshold,startTime=initTime, G=G)
	return simName, NumSteps, dt, sys

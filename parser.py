from body import *
from system import *



def parseNbodySystem(filename):
	
	p = {'simName':'none',\
		  'outputfile':'none',\
		  'bodies':[],\
		  'sysName':'none',\
		  'errThreshold':0,\
		  'G':0,\
		  'NumSteps':0,\
		  'dt':0}
	
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
		 		p['simName'] = value
		 		print "Simulation name set to %s" % p['simName']
		 	if type == 'outputfilename':
		 		p['outputfile'] = value
		 		print "Output filename set to %s" % p['outputfile']
		 	elif type == 'seed':
		 		p['seed'] = int(value)
		 		print "Seed set to %i" % p['seed']
		 	elif type == 'numSteps':
		 		p['NumSteps'] = int(value)
		 		print "Number of steps to calculate set to %i" % p['NumSteps']
		 	elif type == 'dt':
		 		p['dt'] = double(value)
		 		print "Time step set to %g" % p['dt']
		 	elif type == 'G':
		 		p['G'] = double(value)
		 		print "Gravitation constant G set to %g" % p['G']
		 	elif type == 'errorThreshold':
		 		p['errThreshold'] = double(value)
		 		print "Error threshold set to %g" % p['errThreshold']
		 elif mode == 'world':
		 	# Do world reading stuff
		 	# Possible values:
		 	# name initTime
		 	type,value = line.replace(' ','').split('=')
		 	if type == 'name':
		 		p['sysName'] = value
		 		print "System Name set to %s" % p['sysName']
		 	elif type == 'initTime':
		 		p['initTime'] = double(value)
		 		print "System Starting Time set to %g" % p['initTime']
		 elif mode == 'body':
		 	# Load Body
		 	a = Body();
		 	a.load(line)
		 	p['bodies'].append(a)
		 	print "Loaded Body " + str(a)
	
	print "------FINISHED READING FROM FILE------"
	file.close()
	return p

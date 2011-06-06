#!/usr/bin/python
from visual import * # Vpython for 2.7 needed 

#sys =  # This must contain the system to be visualized?
bodies = []
file = open("defaultOut")
readbody = False
for line in file:
	if line.strip() == 'SIMULATION START':
		readbody = True
		print line
	elif line.strip)( == 'SIMULATION END':
		print " File end "
		break
	elif readbody:
		continue
file.close()

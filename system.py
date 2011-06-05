from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *
from randStuff import *

class System:
    def __init__(self,bodies=[],name='',softenLength=0,startTime=0,G=6.7e-11):
        self.name = name
        self.softenLengthSqrd = softenLength**2 # distance below which the gravitational interaction is suppressed
        self.time=startTime;
        self.G = G
        self.bodies = bodies

    def load(self,inpString):
        "Takes input string of format from detailed() output"
        lines = inpString.split('\n')
        self.name = lines[0].split()[0]
        self.time = float(lines[0].split()[1])
        for line in lines[1:]:
            a = Body()
            a.load(line)
            self.bodies.append(a)
    
    def centerBodies(self):
        "Shift all bodies so center of position is at origin"
        center = self.getCenter()
        for body in self.bodies:
            body.pos -= center
            
    def getCenter(self):
    	"Returns vector for center of position of all bodies"
        p=array([0,0,0],double)
        for body in self.bodies:
            p+= body.pos
        p /= len(self.bodies)
        return p

    # Random System Creation ---------------------
    def createRandomBodies(self,n):
        self.bodies = []
        for i in range(0,n):
            self.bodies.append(self.createRandomBody())
        self.centerBodies()
    def createRandomBody(self): # Not yet random
        a = Body()
        a.name = randShortName()
        a.pos = randArr3(-3,3)
        a.vel = randArr3(-1,1)
        return a
    # END Random System Creation ---------------------
    
    def stepMany(self,numSteps,dt):
        for i in range(0,numSteps):
            self.step(dt)
            yield i
            
    # Step Function
    def step(self,dt):
    	  # Check to see if this is correct enough, or pos = initpos + initvel*dt + 0.5*dt*dt*accel is better, with buffer array
        # Update velocities
        for a,b in self.AllBodyRelationships():
            d =  (a.pos-b.pos)# Distance between, d vector
            d2 = vdot(d,d) # |r|^2 scalar
            
            # d * G*m*m/(r^2+e^2)^(3/2)
            if (a.mass == 0):
            	# Assume mass of a is negligable
            	F = d * self.G * b.mass / (d2+self.softenLengthSqrd)**(1.5) 
            	a.vel -= F*dt
            elif (b.mass == 0):
            	# Assume mass of a is negligable
            	F = d * self.G * a.mass / (d2+self.softenLengthSqrd)**(1.5) 
            	b.vel += F*dt
            else:
		         F = d * self.G * a.mass * b.mass / (d2+self.softenLengthSqrd)**(1.5)
		         a.vel -= F*dt * b.mass / (a.mass+b.mass)
		         b.vel += F*dt * a.mass / (a.mass+b.mass)                
        
        # Update positions
        for body in self.bodies:
            body.pos += body.vel*dt

        # Update time
        self.time += dt

    def getTotalEnergy(self):
        "Get Total Energy = Potential + Kinetic of system"
        W = self.getPotentialEnergy() # Add total potential Energy
        W += self.getKineticEnergy()
        return W

    def getKineticEnergy(self):
        return sum(body.getKineticEnergy() for body in self.bodies)
    
    def getPotentialEnergy(self):
        #W=-0.5*sum(G*m*m/|d|)
        W = 0
        for a,b in self.AllBodyRelationships():
            d =  (a.pos-b.pos)# Distance between, d
            d2 = vdot(d,d) # |r|^2
            W += -0.5*self.G*a.mass * b.mass / sqrt(d2)
        return W
    
    # Helper functions
    def AllBodyRelationships(self):
        "iterator for every body relationship, no i=j or inverse"
        for i in range(0,len(self.bodies)):
            for j in range(i+1,len(self.bodies)):
                yield (self.bodies[i],self.bodies[j])
    
    def size(self):
    	"Number of bodies in system"
        return len(self.bodies)
    def short(self):
        return "\n".join(body.short() for body in self.bodies)
    def detailed(self):
        result = '%s %g\n' % (self.name, self.time)
        result += "\n".join(body.detailed() for body in self.bodies)
        return result
    def __str__(self):
        result = "%s \t| Time: %g, N: %d, KE: %g PE: %g Total Energy: %g\n" \
              % (self.name, self.time,\
                 self.size(), self.getKineticEnergy(), \
                 self.getPotentialEnergy(), self.getTotalEnergy())
        result += "\n".join(body.__str__() for body in self.bodies)
        return result

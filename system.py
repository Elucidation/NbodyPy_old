from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *

class System:
    def __init__(self,bodies=[],n=0,name='',softenLength=0,startTime=0):
        self.name = name
        self.softenLength = softenLength # distance below which the gravitational interaction is suppressed
        self.time=startTime;
        # save softenLength**2 instead
        if bodies == []:
            self.createRandomBodies(n)
        else:
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
        

    # Random System Creation
    def createRandomBodies(self,n):
        self.bodies = []
        for i in range(0,n):
            self.bodies.append(self.createRandomBody())
    def createRandomBody(self): # Not yet random
        return Body( 0,0,0, \
                  0,0,0, \
                  1 , 'random')

    def stepMany(self,numSteps,dt):
        for i in range(0,numSteps):
            self.step(dt)
            yield i
            
    # Step Function
    def step(self,dt):
        # Update velocities
        for a,b in self.AllBodyRelationships():
            d =  (a.pos-b.pos)# Distance between, d
            d2 = vdot(d,d) # |r|^2
            # d * G*m*m/(r^2+e^2)^(3/2)
            F = d * a.mass * b.mass / (d2+self.softenLength**2)**(1.5)
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
            W += -0.5*a.mass * b.mass / sqrt(d2)
        return W
    
    # Helper functions
    def AllBodyRelationships(self):
        "iterator for every body relationship"
        for i in range(0,len(self.bodies)):
            for j in range(i+1,len(self.bodies)):
                yield (self.bodies[i],self.bodies[j])
    def size(self):
        return len(self.bodies)
    def short(self):
        result = ''
        for body in self.bodies:
            result += body.short() + "\n"
        return result
    def detailed(self):
        result = '%s %g\n' % (self.name, self.time)
        for body in self.bodies:
            result += body.detailed() + "\n"
        return result
    def __str__(self):
        str = "%s \t| Time: %g, N: %d, KE: %g PE: %g Total Energy: %g\n" \
              % (self.name, self.time,\
                 self.size(), self.getKineticEnergy(), \
                 self.getPotentialEnergy(), self.getTotalEnergy())
        for body in self.bodies:
            str += body.__str__() + "\n"
        return str

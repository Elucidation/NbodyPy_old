from numpy import * # http://numpy.scipy.org/ v1.5.1
from body import *

class System:
    def __init__(self,bodies=[],n=0,name=''):
        self.name = name
        if bodies == []:
            self.createRandomBodies(n)
        else:
            self.bodies = bodies

    # Random System Creation
    def createRandomBodies(self,n):
        self.bodies = []
        for i in range(0,n):
            self.bodies.append(self.createRandomBody())
    def createRandomBody(self): # Not yet random
        return Body( 0,0,0, \
                  0,0,0, \
                  1 , 'random')

    # Step Function
    def step(self,dt):
        # Update velocities
        for i in range(0,len(self.bodies)):
            a = self.bodies[i]
            for j in range(i+1,len(self.bodies)):
                b = self.bodies[j]
                d =  (a.pos-b.pos)# Distance between
                d2 = vdot(d,d)
                if d2>0:
                    F = d * (a.mass * b.mass / (sqrt(d2)*d2))# G*M*m/r^2 * 1/r * d
                else:
                    print " Collision between [%s] and [%s]" % (a,b)
                    F = d * 0
                a.vel += F*dt * b.mass / (a.mass+b.mass)
                b.vel -= F*dt * a.mass / (a.mass+b.mass)
        
        # Update positions
        for body in self.bodies:
            body.pos += body.vel*dt

    # Helper functions
    def size(self):
        return len(self.bodies)
    def __str__(self):
        str = "%s \t| Number of Bodies: %.1f\n" % (self.name,self.size())
        for body in self.bodies:
            str += body.__str__() + "\n"
        return str

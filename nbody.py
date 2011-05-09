#!/usr/bin/python
# Filename: nbody.py

from numpy import * # http://numpy.scipy.org/ v1.5.1

class Body:
    def __init__(self, x=0,y=0,z=0,vx=0,vy=0,vz=0,mass=1,name=''):
        self.name = name
        self.pos = array([x,y,z],double) # Position, type double
        self.vel = array([vx,vy,vz],double) # Velocity
        self.mass = double(mass) # Mass
    def __str__(self):
        return '%s \t| Pos: (%.1f,%.1f,%.1f)\t'\
               'Vel: <%.1f,%.1f,%.1f>\t'\
               'Mass: %.1f' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)

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
        


class Test:
    def test1(self):
        a = Body(name='bob',y=2,mass=3)
        print a
    def test2(self):
        a = Body(name='bob',y=2,mass=3)
        b = Body(name='jill',x=-1,mass=2)
        print a
        print b
    def test3(self):
        a = Body(name='bob',y=2,mass=3)
        b = Body(name='jill',x=-1,vy = 1,mass=2)
        sys = System(bodies=[a, b],name='world')
        print sys
    def test4(self):
        a = System(n=2,name='world')
        print a
    def test5(self):
        a = Body(name='bob',x = 1, vy = 1,mass=3)
        b = Body(name='jill',x = -1, vy = -1,mass=2)
        sys = System(bodies=[a, b],name='world')
        print sys
        sys.step(0.5)
        print sys
        


a = Test()
a.test5()

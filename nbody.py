#!/usr/bin/python
# Filename: nbody.py

class Body:
    def __init__(self, x=0,y=0,z=0,vx=0,vy=0,vz=0,mass=1,name=''):
        self.name = name
        self.x,self.y,self.z = x,y,z # Position
        self.vx,self.vy,self.vz = vx,vy,vz # Velocity
        self.mass = mass # Mass
    def __str__(self):
        return '%s \t| Pos: (%d,%d,%d)\tVel: <%d,%d,%d>\tMass: %d' \
               % (self.name, \
                 self.x,self.y,self.z, \
                 self.vx,self.vy,self.vz, \
                 self.mass)

class System:
    def __init__(self,bodies=[],n=0,name=''):
        self.name = name
        if bodies == []:
            self.bodies = createRandomBodies(n)
        else:
            self.bodies = bodies
    def createRandomBodies(self,n):
        for i in range(0,n):
            self.bodies << createRandomBody()
    def createRandomBody(self): # Not yet random
        k = Body( 0,0,0, \
                  0,0,0, \
                  1 , 'random')
    def 
    def size(self):
        return len(self.bodies)
    def __str__(self):
        str = "%s \t| Number of Bodies: %d\n" % (self.name,self.size())
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


a = Test()
a.test3()

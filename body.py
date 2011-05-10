from numpy import * # http://numpy.scipy.org/ v1.5.1

class Body:
    def __init__(self, x=0,y=0,z=0,vx=0,vy=0,vz=0,mass=1,name=''):
        self.name = name
        self.pos = array([x,y,z],double) # Position, type double
        self.vel = array([vx,vy,vz],double) # Velocity
        self.mass = double(mass) # Mass
    def setPos(self,x,y,z):
        self.pos = array([x,y,z],double)
    def setVel(self,vx,vy,vz):
        self.vel = array([vx,vy,vz],double)

    def getKineticEnergy(self):
        "Kinetic energy of body 0.5*m*v^2"
        return 0.5*self.mass*(vdot(self.vel,self.vel))
    def __str__(self):
        return '[%s(%.1f,%.1f,%.1f)'\
               '<%.1f,%.1f,%.1f>'\
               'm%g]' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)
    def prettyprint(self):
        return '%s \t| Pos: (%.1f,%.1f,%.1f)\t'\
               'Vel: <%.1f,%.1f,%.1f>\t'\
               'Mass: %g' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)
    def detailed(self):
        return '%s %g %g %g '\
               '%g %g %g '\
               '%g' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)
    def load(self,inpString):
        "ex: bob 0.0777648 9.06124 0 0.117897 0.878156 0 1"
        self.name = inpString.split()[0]
        self.pos[0],self.pos[1],self.pos[2], \
        self.vel[0],self.vel[1],self.vel[2], \
        self.mass = map(double,inpString.split()[1:])
    def short(self):
        "Just the positions and velocities"
        return '%.1f %.1f %.1f '\
               ' %.1f %.1f %.1f '\
               % (self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2])

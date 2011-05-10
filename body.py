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

    def getEnergy(self):
        "Kinetic energy of body 0.5*m*v^2"
        return 0.5*self.mass*(self.vel**2)
    def __str__(self):
        return '[%s(%.1f,%.1f,%.1f)'\
               '<%.1f,%.1f,%.1f>'\
               'm%.1f]' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)
    def prettyprint(self):
        return '%s \t| Pos: (%.1f,%.1f,%.1f)\t'\
               'Vel: <%.1f,%.1f,%.1f>\t'\
               'Mass: %.1f' \
               % (self.name, \
                 self.pos[0],self.pos[1],self.pos[2], \
                 self.vel[0],self.vel[1],self.vel[2], \
                 self.mass)



class Body:
    def __init__(self, x=0,y=0,z=0,vx=0,vy=0,vz=0,mass=1):
        self.x,self.y,self.z = x,y,z # Position
        self.vx,self.vy,self.vz = vx,vy,vz # Velocity
        self.mass = mass # Mass

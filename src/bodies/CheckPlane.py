from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body
from raytrace.src.bodies.Plane import Plane

def floor(x):
    if x < 0:
        return int(x - 1)
    else:
        return int(x)

class CheckPlane(Plane):
    
    def set_colors(self, c1, c2):
        self.c1 = c1
        self.c2 = c2
        return self
    
    def set_orientation(self, orientation):
        self.oX = (orientation - self._origin).norm()
        self.oY = self._normal.cross(self.oX).norm()
        return self
    
    def __init__(self,
            normal = Vector(0.0,1.0,0.0),
            origin = Vector(0.0,0.0,0.0),
            orientation = Vector(1.0,0.0,0.0),
            c1 = Color(0.01,0.01,0.01),
            c2 = Color(0.99,0.99,0.99)):
        """Initializes plane and plane colors."""
        Plane.__init__(self, normal, origin)
        self.set_orientation(orientation)
        self.set_colors(c1,c2)

    def get_color(self, point):
        """Returns color of plane at the point."""
        
        # we need to find distance to point from plane origin
        # in terms of oX and oY (plane orientation vectors)
        # get d: the vector from plane origin to poi
        # d dot orientation vectors is length in that direction
        d = point - self._origin
        lenx = floor(d.dot(self.oX))
        leny = floor(d.dot(self.oY))
        
        dist = abs(lenx + leny) % 2
        if dist == 0:
            return self.c1.dup()
        else:
            return self.c2.dup()


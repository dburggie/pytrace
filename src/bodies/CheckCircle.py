from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body
from raytrace.src.bodies.CheckPlane import CheckPlane

def floor(x):
    if x < 0:
        return int(x - 1)
    else:
        return int(x)

class CheckCircle(CheckPlane):
    
    def set_orientation(self, orientation):
        self.oX = (orientation - self._origin).norm()
        self.oY = self._normal.cross(self.oX).norm()
        return self
    
    def __init__(self,
            r = 1.0,
            normal = Vector(0.0,1.0,0.0),
            origin = Vector(0.0,0.0,0.0),
            orientation = Vector(1.0,0.0,0.0),
            c1 = Color(0.01,0.01,0.01),
            c2 = Color(0.99,0.99,0.99)):
        """Initializes plane and plane colors."""
        
        CheckPlane.__init__(self, normal, origin, orientation, c1, c2)
        self.origin = origin
        self.set_orientation(orientation)
        self.r = r
        self.R = r ** 2.0
    
    def intersection(self, ray):
        distance = CheckPlane.intersection(self, ray)
        if distance < 0.0:
            return distance
        else:
            point = ray.follow(distance).add(self.origin, -1.0)
        dx = point.dot(self.oX)
        dy = point.dot(self.oY)
        if dx ** 2.0 + dy ** 2.0 > self.R:
            return -1.0
        else:
            return distance
    


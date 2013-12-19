from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body
from Sphere import Sphere

class hmSphere(Sphere):
    """Half-mirrored sphere."""
    
    def set_orientation(self, o):
        self.orientation = o.norm()
        return self
    
    
    
    def set_color(self, c):
        self.color = Color
        return self
    
    
    
    def set_reflectivity(self, mirror, non_mirror):
        self._mr = max(0.0,min(1.0,mirror))
        self._nr = max(0.0,min(1.0,non_mirror))
        return self
    
    
    
    def reflectivity(self, point):
        if self.orientation.dot(point - self.center) > 0.0:
            return self._mr
        else:
            return self._nr
    
    
    
    def __init__(self, center = Vector(0.0,0.0,0.0),
            radius = 1.0,
            color = Color(),
            orientation = Vector(0.0,1.0,0.0)):
        Sphere.set_position(self, center)
        Sphere.set_radius(self, radius)
        Sphere.set_color(self, color)
        self.set_orientation(orientation)
        self.set_reflectivity(0.9,0.1)
    
    

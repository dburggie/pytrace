from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body
from Sphere import Sphere

class hmSphere(Sphere):
    """Half-mirrored sphere."""
    def __init__(self, center = Vector(0.0,0.0,0.0),
            radius = 1.0,
            color = Color(),
            orientation = Vector()):
        Sphere.__init__(self, center, radius, color)
        self.orientation = orientation.norm()
    
    def set_orientation(self, o):
        self.orientation = o.norm()
    
    def reflectivity(self, point):
        if self.orientation.dot(point - self.center) > 0.0:
            return 0.9
        else:
            return 0.1

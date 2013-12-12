import bounds
from Vector import Vector
from Ray import Ray
from Body import Body
from Interface import Interface

class Plane(Body):
    n = Vector(0.0,1.0,0.0)
    o = Vector()
    c = [0.05,0.05,0.05]
    
    def __init__(self, normal, origin, color = [0.001,0.001,0.001]):
        self.n = normal
        self.o = origin
        self.c = color
    
    def p(self):
        return 'Plane'
    
    def get_color(self, point):
        return self.c.dup()
    
    def normal(self, point):
        return self.n.dup()
    
    def intersection(self, ray):
        """Returns positive distance to target."""
        cosine = self.n.dot(ray.d)
        if cosine < bounds.too_small:
            return -1.0
        # find magnitudes of d and o projected onto n
        # (o - p) dot n / d dot n
        t = (ray.o.x - self.o.x) * self.n.x
        t = t + (ray.o.y - self.o.y) * self.n.y
        t = t + (ray.o.z - self.o.z) * self.n.z
        if t < bounds.too_close or t > bounds.too_far:
            return -1.0
        return t / cosine
        

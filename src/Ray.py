from Vector import Vector
from Interface import Interface

class Ray:
    """This class handles ray manipulation."""
    o = Vector(0.0,0.0,0.0)
    d = Vector(0.0,1.0,0.0)
    
    def __init__(self, o = Vector(0.0,0.0,0.0), d = Vector(0.0,1.0,0.0):
        self.o = o
        self.d = d
    
    def set_origin(self, origin):
        self.o = origin
        return self
    
    def follow(self, d):
        return Vector(self.o.x + self.d.x * d,
                self.o.y + self.d.y * d,
                self.o.z + self.d.z * d)
    
    def set_direction(self, direction):
        self.d = direction
        return self
    
    def reflect(self, interface):
        # o = p, d = d - 2 (n dot d) n
        self.o = interface.poi
        c = -2.0 * self.d.dot(interface.normal)
        n = interface.normal
        self.d.trans(c * n.x, c * n.y, c * n.z).norm()
        return self
    
    

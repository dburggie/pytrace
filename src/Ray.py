from Vector import Vector

class Ray:
    """This class handles ray manipulation."""
    o = Vector(0.0,0.0,0.0)
    d = Vector(0.0,1.0,0.0)
    
    def __init__(self, o = Vector(0.0,0.0,0.0), d = Vector(0.0,1.0,0.0)):
        self.o = o
        self.d = d.norm()
    
    def __eq__(self, r):
        if self.o == r.o and self.d == r.d:
            return True
        else:
            return False
    
    def dup(self):
        return Ray(self.o.dup(), self.d.dup())
    
    def set_origin(self, origin):
        self.o = origin
        return self
    
    def set_direction(self, direction):
        self.d = direction.norm()
        return self
    
    def follow(self, d):
        # could rewrite as:
        #   return self.o.dup().add(self.d, d)
        return Vector(self.o.x + self.d.x * d,
                self.o.y + self.d.y * d,
                self.o.z + self.d.z * d)
    
    def reflect(self, point, normal):
        # o = p, d = d - 2 (n dot d) n
        self.o = point
        s = -2.0 * self.d.dot(normal)
        self.d.add(normal, s).norm()
        return self
    
    

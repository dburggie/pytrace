from rand import rand

class Vector:
    """This handles vector math and manipulation."""
    x = 0.0
    y = 0.0
    z = 0.0
    l = 0.0
    
    def length(self):
        """Calculates vector length."""
        self.l = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
    def __init__(self, x = 0.0, y = 1.0, z = 0.0):
        """Initialize vector with x,y,z coordinates."""
        self.x = x
        self.y = y
        self.z = z
        self.length()
    
    def __sub__(self, vector):
        """Overload '-' operator for vector differences."""
        return Vector(
                self.x - vector.x,
                self.y - vector.y,
                self.z - vector.z
                )
    
    def dup(self):
        """Create copy of vector."""
        return Vector(self.x, self.y, self.z)
    
    def copy(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z
        self.l = vector.l
        return self
    
    def add(self, vector, scalar = 1.0):
        """Translate vector by vector addition"""
        self.x += vector.x * scalar
        self.y += vector.y * scalar
        self.z += vector.z * scalar
        self.length()
        return self
    
    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        self.l *= scalar
        return self
    
    def trans(self, x, y, z):
        """Translate vector by x,y,z offsets."""
        self.x += x
        self.y += y
        self.z += z
        self.length()
        return self
    
    def norm(self):
        """Normalize vector to length 1."""
        self.length()
        if abs(self.l) <  bounds.very_small:
            return self # why did you normalize a zero vector?
        while abs(self.l - 1.0) > bounds.small:
            self.x /= l
            self.y /= l
            self.z /= l
            self.length()
        return self
    
    def dot(self, vector):
        """Calculate dot product of this vector and another."""
        return self.x * vector.x + self.y * vector.y + self.z * vector.z
    
    def cross(self, vector):
        """Returns cross product of this vector by another."""
        return Vector(
                self.y * vector.z - self.z * vector.y,
                self.z * vector.x - self.x * vector.z,
                self.x * vector.y - self.y * vector.x
                )
    
    def delta(self, d):
        """slightly nudges direction of vector."""
        dx,dy,dz = 1,1,1
        while dx ** 2 + dy ** 2  + dz ** 2 > 1.0:
            dx = rand(2) - 1.0
            dy = rand(2) - 1.0
            dz = rand(2) - 1.0
        dx *= d
        dy *= d
        dz *= d
        self.trans(dx,dy,dz)
        
    
    def p(self):
        return "[{0},{1}.{2}]".format(self.x, self.y, self.z)







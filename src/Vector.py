from rand import rand
import bounds

class Vector:
    """This handles vector math and manipulation."""
    x = 0.0
    y = 0.0
    z = 0.0
    
    def dot(self, vector):
        """Calculate dot product of this vector and another."""
        return self.x * vector.x + self.y * vector.y + self.z * vector.z
    
    def length(self):
        """Calculates vector length."""
        return self.dot(self)# ** 0.5
    
    def __init__(self, x = 0.0, y = 1.0, z = 0.0):
        """Initialize vector with x,y,z coordinates."""
        self.x = x
        self.y = y
        self.z = z
    
    def __sub__(self, vector):
        """Overload '-' operator for vector differences."""
        return Vector(
                self.x - vector.x,
                self.y - vector.y,
                self.z - vector.z
                )
    
    def __eq__(self, v):
        """Overload '=' operator for vector equality."""
        # treat the vectors as equal if they are very close together
        if (self - v).length() < bounds.very_small:
            return True
        else:
            return False
    
    def dup(self):
        """Create copy of vector."""
        return Vector(self.x, self.y, self.z)
    
    def copy(self, vector):
        self.x = vector.x
        self.y = vector.y
        self.z = vector.z
        return self
    
    def add(self, vector, scalar = 1.0):
        """Translate vector by vector addition"""
        self.x += vector.x * scalar
        self.y += vector.y * scalar
        self.z += vector.z * scalar
        return self
    
    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    
    def trans(self, x, y, z):
        """Translate vector by x,y,z offsets."""
        self.x += x
        self.y += y
        self.z += z
        return self
    
    def norm(self):
        """Normalize vector to length 1."""
#        l = (self.x * self.x + self.y * self.y + self.z * self.z ) ** 0.5
        l = (self.x * self.x + self.y * self.y + self.z * self.z ) ** -0.5
        if l <  bounds.very_small:
            raise self # why did you normalize a zero vector?
#        self.x /= l
#        self.y /= l
#        self.z /= l
        self.x *= l
        self.y *= l
        self.z *= l
        return self
    
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
        return self
    
    def p(self):
        return "[{0},{1}.{2}]".format(self.x, self.y, self.z)







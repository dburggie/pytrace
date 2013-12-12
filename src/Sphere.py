import bounds
from Vector import Vector
from Body import Body

class Sphere(Body):
    
    center = Vector()
    radius = 0.0
    R = 0.0
    color = [0.01,0.01,0.01]
    
    def __init__(self, center, radius, color):
        self.center = center
        self.radius = radius
        self.R = radius ** 2
        self.color = color
    
    def p(self):
        return 'Sphere'
    
    def get_color(self, point):
        return self.color.dup()
    
    def normal(self, point):
        return (point - self.center).norm()
    
    def reflectivity(self, point):
        pass
    
    def intersection(self, ray):
        """Returns distance from along to closest intersection with sphere."""
        # ray intersection with sphere:
        #   O: ray origin
        #   D: ray direction
        #   C: ray center
        #   R: square of sphere radius
        #   S: ray from sphere center to ray origin (S = O - C)
        #   SS: S dot S
        #   SD: S dot D
        #   t: distance to intersection
        #   formula:
        #       t = -SD +/- (SD**2 + R - SS)**0.5
        
        S = ray.o - self.center
        
        # do a dot product the long way
        SD = S.dot( ray.d )
        
        # do a dot product the long way
        SS = S.dot(S)
        
        if SS > bounds.too_far:
            return -1.0
        
#        print ""
#        print "ray on sphere:"
#        print "    radius:   {}".format(self.radius)
#        print "    distance: {}".format(SS)
#        print "    cosine:   {}".format(SD)
#        print ""
        
        radical = SD ** 2 + self.R - SS
        
        if radical < 0.0:
            return -1.0
        
        radical **= 0.5
        hit = -1 * SD - radical
        
        if hit < bounds.too_small:
            hit = -1 * SD + radical
            if hit < bounds.too_small:
                return -1.0
            else:
                return hit
        else:
            return hit
        
        
        

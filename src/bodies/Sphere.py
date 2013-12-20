from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body

class Sphere(Body):
    
    center = Vector()
    radius = 0.0
    R = 0.0
    color = [0.01,0.01,0.01]
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'Sphere'
    
    def set_position(self, c):
        self.center = c
        return self
    
    def set_radius(self, r):
        self.radius = r
        self.R = r ** 2.0
        return self
    
    def set_color(self, c):
        self.color = c
        return self
    
    def get_color(self, point):
        """Returns color of body at given point."""
        return self.color.dup()
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        return (point - self.center).norm()
    
    def set_reflectivity(self, r):
        self._r = max(0.0,min(1.0,r))
        return self
    
    def reflectivity(self, point):
        """Returns percentage of brightness due to specular reflection."""
        return self._r
    
    def __init__(self, center, radius, color = Color()):
        self.set_position(center)
        self.set_radius(radius)
        self.set_color(color)
        self.set_reflectivity(0.2)
    
    # Intersection of ray with a sphere boils down to the solutions to a 
    # quadratic vector equation.
    #
    # Let S be the vector from sphere center to ray origin, D be ray direction
    # and R be the square of the radius of the sphere
    #
    # Then call S dot S SS, and, similarly, SD is S dot D
    #
    # Now the intersections occur at the following distances:
    #     -SD +/- sqrt(SD**2 + R - SS)
    def intersection(self, ray):
        """Returns distance from ray to closest intersection with sphere."""
        
        S = ray.o - self.center
        SD = S.dot( ray.d )
        SS = S.dot(S)
        
        # no hit if sphere is really far away
        if SS > bounds.too_far ** 2:
            return -1.0
        
        radical = SD ** 2 + self.R - SS
        # negative radical implies no solutions
        if radical < 0.0:
            return -1.0
        
        radical **= 0.5
        hit = -1 * SD - radical
        
        if hit < bounds.too_close:
            hit = -1 * SD + radical
            if hit < bounds.too_small:
                return -1.0
            else:
                return hit
        else:
            return hit
        
        
        

from raytrace.src import bounds
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray
from raytrace.src.Color import Color
from raytrace.src.Body import Body

class Plane(Body):
    _normal = Vector(0.0,1.0,0.0)
    _origin = Vector()
    _color = [0.05,0.05,0.05]
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'Plane'
    
    def set_position(self, p):
        self._origin = p
        return self
    
    def set_color(self, c):
        self._color = c
        return self
    
    def get_color(self, point):
        """Returns color of body at given point."""
        return self._color.dup()
    
    def set_normal(self, n):
        self._normal = n.norm()
        return self
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        return self._normal.dup()
    
    def set_reflectivity(self, r):
        self._r = r
        return self
    
    def reflectivity(self, point):
        """Returns percentage of brightness due to specular reflection."""
        return self._r
    
    def __init__(self, normal, origin, color = [0.001,0.001,0.001]):
        self.set_normal(normal)
        self.set_position(origin)
        self.set_color(color)
        self.set_reflectivity(0.2)
    
    # intersection of a ray with a plane is pretty easy:
    #  * first, find the projection of ray direction onto the normal
    #      * this is the portion of the velocity on the shortest path to plane
    #  * divide the length of the shortest vector from plane to ray origin
    #            by the length of the projection vector above
    #      * get this vector by projecting ray origin minus plane origin onto
    #                the plane normal
    #  * now you have the distance along the ray to the point of intersection!
    #      * this distance might be negative. Take this into account.
    def intersection(self, ray):
        """Returns positive distance to target (or negative if no hit)."""
        d_proj = self._normal.dot(ray.d)
        if abs(d_proj) < bounds.too_small:
            return -1.0
        s_proj = (self._origin - ray.o).dot(self._normal)
        if d_proj * s_proj < 0.0:
            # ray going away from plane
            return -1.0
        else:
            return s_proj / d_proj
        

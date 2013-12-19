import bounds
from Vector import Vector
from Ray import Ray
from Body import Body
from Interface import Interface

class Plane(Body):
    _normal = Vector(0.0,1.0,0.0)
    _origin = Vector()
    _color = [0.05,0.05,0.05]
    
    def __init__(self, normal, origin, color = [0.001,0.001,0.001]):
        self._normal = normal.norm()
        self._origin = origin
        self._color = color
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'Plane'
    
    def get_color(self, point):
        """Returns color of body at given point."""
        return self._color.dup()
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        return self._normal.dup()
    
    def reflectivity(self, point):
        """Returns percentage of brightness due to specular reflection."""
        return 0.0
    
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
        s = self._origin - ray.o
        if s.dot(ray.d) < 0:
            # this means ray is going away from plane
            return -1.0
        return abs(s.dot(self._normal) / self._normal.dot(ray.d))
        

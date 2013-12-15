from Vector import Vector

class Body:
    """Container class for 3d objects."""
    
    def __init__(self):
        pass
    
    def p(self):
        """Returns the name of the type of body this is."""
        return 'Body'
    
    def get_color(self, point):
        """Returns color of body at given point."""
        pass
    
    def normal(self, point):
        """Returns normal vector of body at given point."""
        pass
    
    def reflectivity(self, point):
        """Returns percentage of brightness due to specular reflection."""
        pass
    
    def intersection(self, ray):
        """Returns distance at which ray intersects body."""
        pass

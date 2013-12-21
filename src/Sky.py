from py3D import Vector, Color

class Sky:
    """Class that describes the sky."""
    
    def __init__(self, light = Vector(0.0,1.0,0.0),
            color = Color(0.2,0.2,0.9)):
        self.light = light.norm()
        self.color = color
    
    def get_color(self, ray):
        d = max(ray.d.dot(self.light), 0)
        return self.color.dup().gamma(1 - d ** 20)
    
    def get_light(self):
        return self.light.dup()

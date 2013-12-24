from py3D import Vector, Color

_default_exponent = 20.0

class Sky:
    """Class that describes the sky."""
    
    def __init__(self, light = Vector(0.0,1.0,0.0),
            color = Color(0.2,0.2,0.9)):
        self.light = light.norm()
        self.color = color
        self._exp = _default_exponent
    
    def set_brightness(self, exp):
        """Sets brightness of sun: low is brighter."""
        self._exp = exp
        return self
    
    def get_color(self, ray, exp = None):
        if exp == None:
            exp = _default_exponent
        d = max(ray.d.dot(self.light), 0)
        return self.color.dup().gamma(1 - d ** self._exp)
    
    def get_light(self):
        return self.light.dup()

import bounds
from Sky import Sky
from Interface import Interface
from py3D import Body, Color, Ray, Vector


class World:
    """This class holds body/camera/view information and performs raytrace."""
    
    
    _bodies = []
    _sky = Color()
    _interface = Interface()
    _light = Vector().norm()
    _base_brightness = 0.2
    
    
    
    def __init__(self, bodies = [], sky = Sky()):
        self._bodies = bodies
        self._sky = sky
        self._light = sky.get_light()
        interface = Interface()
        self._base_brightness = 0.2
    
    
    
    def add_body(self, body):
        self._bodies.append(body)
        return self
    
    
    
    def set_sky(self, sky):
        self._sky = sky
        return self
    
    
    
    def get_sky(self, ray):
        return self._sky.get_color(ray)
    
    def get_light(self):
        return self._light.dup()
    
    def set_base_brightness(self, b):
        self._base_brightness = b
        return self
    
    def trace(self, ray, last_hit = None):
        """Finds first interaction of a ray within the world."""
        
        self._interface.reset()
        
        for bodies in self._bodies:
        
            # check for intersection of ray with body
            distance = bodies.intersection(ray)
            if distance < 0.0:
                continue
            
            # move on if we're interacting with our starting point
            if bodies == last_hit and distance < bounds.too_close:
                continue
            
            # if we've got a hit, register it if it's closer
            self._interface.hit(bodies, distance)
        # end for
        
        # register the rest of our interface
        self._interface.register_hit(ray)
        
        return self._interface
    
    
    
    def shade(self, interface):
        """Detects amount of illumination at point."""
        ray = Ray( interface._poi, self.get_light() )
        lambertian = self._light.dot(interface._normal)
        if lambertian < self._base_brightness:
            return self._base_brightness
        for bodies in self._bodies:
            distance = bodies.intersection(ray)
            if distance < 0.0:
                continue
            if bodies != interface._body or distance > bounds.too_small:
                lambertian = self._base_brightness
                break
        return lambertian
    
    
    
    def sample(self, ray, last_hit = None, depth = 0):
        """Recursively traces ray within world."""\
        
        # check trace depth boundary
        if depth == bounds.max_depth:
            return Color(0.001,0.001,0.001)
        
        # get a trace interface
        i = self.trace(ray, last_hit)
        
        # detect hitting the sky
        if i._body == None:
            return self.get_sky(ray)
        
        # handling color of pixel:
        #   we need to adjust the color based on:
        #       1) lambertian factor: angle of surface to light source
        #       2) surface has direct line of sight to light source (shadow)
        #       3) specular reflection and refraction
        #   thus a formula:
        #       Parameters:
        #           B: base brightness
        #           S: specularity of interface
        #               (1-S) is thus power of diffuse brightness
        #           L: lambertian factor
        #           R: color in reflected direction
        #           C: color at this interface
        #       Formula:
        #           L = Normal.dot(Light)
        #           if L < 0 or in shadow: L = B
        #           (1-S)*L*C + S*R
        
        sp = i._body.reflectivity(i._poi)
        dp = 1.0 - sp
        L = self.shade(i)
        color = i._color.dim(L).dim(dp)
        return color + self.sample(ray.reflect(i._poi, i._normal), 
                i._body, depth + 1).dim(sp)
    
    
    

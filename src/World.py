import bounds
from Sky import Sky
from Interface import Interface
from py3D import Body, Color, Ray, Vector
from refract import sinSnell, cosSnell, fresnel


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
        ray = Ray( interface.poi, self.get_light() )
        lambertian = self._light.dot(interface.normal)
        
        if lambertian < self._base_brightness:
            return self._base_brightness
        
        for bodies in self._bodies:
            distance = bodies.intersection(ray)
            if distance < 0.0:
                continue
            if bodies != interface.body or distance > bounds.too_small:
                lambertian = self._base_brightness
                break
        
        return lambertian
    
    
    
    def sample(self, ray, index = 1.0, depth = 0, last_hit = None):
        """Recursively traces ray within world."""
        
        # check trace depth boundary
        if depth == bounds.max_depth:
            return Color(0.001,0.001,0.001)
        
        # get a trace interface
        i = self.trace(ray, last_hit)
        
        # detect hitting the sky
        if i.body == None:
            return self.get_sky(ray)
        
        # shade point
        L = self.shade(i)
        
        # add specular highlight if matte surface
        if i.matte:
            ray.reflect(i.poi, i.normal)
            highlight = max(0.0,ray.d.dot(self.get_light()))
            highlight **= i.exp
            return i.color.dim(L).gamma(1 - highlight)
        
        # if not matte, we do specular reflection
        else:
            
            cos_i = abs(ray.d.dot(i.normal))
            R = i.body.reflectivity(i.poi)
            D = 1 - R
            Ps = R + D * ( (1 - cos_i) ** i.exp )
            Pt = 1.0 - Ps
            
            color = i.color.dim(L).dim(Pt)
            return color + self.sample(ray.reflect(i.poi, i.normal), index,
                    depth + 1, i.body).dim(Ps)
    
    
    

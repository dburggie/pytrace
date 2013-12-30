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
    
    
    
    def sample(self, ray, index = 1.0, depth = 0, last_hit = None):
        """Recursively traces ray within world."""\
        
        # check trace depth boundary
        if depth == bounds.max_depth:
            return Color(0.001,0.001,0.001)
        
        # get a trace interface
        i = self.trace(ray, last_hit)
        
        # detect hitting the sky
        if i._body == None:
            return self.get_sky(ray)
        
        # here's what happens at an interface:
        #   find out specular power using fresnel function Ps
        #   use specular power to find transmissive power Pt
        #   get body's opacity O
        #   if 0 != 1.0: calculate refraction ray
        #       color = (1 - O) * Pt * sample(refraction)
        #   color = color + shade * O * Pt * bodycolor
        #   color = color + Ps * sample(reflection)
        
        cos_i = abs(ray.d.dot(i._normal))
        R = i._body.reflectivity(i._poi)
        D = 1 - R
        Ps = R + D * (1 - cos_i) ** 2
        Pt = 1.0 - Ps
        
        L = self.shade(i)
        color = i._color.dim(L).dim(Pt)
        return color + self.sample(ray.reflect(i._poi, i._normal), index,
                depth + 1, i._body).dim(Ps)
    
    
    

import bounds
from Color import Color
from Vector import Vector
from Ray import Ray
from Body import Body
from Sphere import Sphere
from Plane import Plane
from Interface import Interface

base_brightness = 0.2
base_specularity = 0.5

class World:
    
    
    
    bodies = []
    sky = Color()
    interface = Interface()
    light = Vector().norm()
    
    
    
    def __init__(self, bodies = [], sky = Color(), light = Vector()):
        self.bodies = bodies
        self.sky = sky
        self.light = light.norm()
        interface = Interface()
    
    
    
    def add_body(self, body):
        self.bodies.append(body)
        return self
    
    
    
    def set_sky(self, color):
        self.sky = color
        return self
    
    
    
    def get_sky(self):
        return self.sky.dup()
    
    def get_light(self):
        return self.light
    
    def trace(self, ray, last_hit = None):
        """Finds first interaction of a ray within the world."""
        
        self.interface.reset()
        
        for bodies in self.bodies:
        
            # check for intersection of ray with body
            distance = bodies.intersection(ray)
            if distance < 0.0:
                continue
            
            # move on if we're interacting with our starting point
            if bodies == last_hit and distance < bounds.too_close:
                continue
            
            # if we've got a hit, register it if it's closer
            self.interface.hit(bodies, distance)
        # end for
        
        # register the rest of our interface
        self.interface.register_hit(ray)
        
        return self.interface
    
    
    
    def shade(self, interface):
        """Detects amount of illumination at point."""
        # definitely make this better than a single hardcoded lightsource
        ray = Ray( interface.poi, self.get_light() )
        lambertian = (1.0 - base_specularity) * self.light.dot(interface.normal)
        if lambertian < base_brightness:
            return base_brightness
        for bodies in self.bodies:
            distance = bodies.intersection(ray)
            if distance < 0.0:
                continue
            if bodies != interface.body or distance > bounds.too_small:
                lambertian = base_brightness
                break
        return lambertian
    
    
    
    def sample(self, ray, last_hit = None, depth = 0):
        """Recursively traces ray within world."""\
        
        # check trace depth boundary
        if depth == bounds.max_depth:
            return Color(0.001,0.001,0.001)
        
        # get a trace interface
        i = self.trace(ray, last_hit).dup()
        
        # detect hitting the sky
        if i.body == None:
            return self.get_sky()
        
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
        
        color = i.color.dup()
        
#        sp = base_specularity
#        dp = 1.0 - sp
#        L = self.shade(i)
#        color = i.color.dim(L).dim(dp)
#        color = color + self.sample(ray.reflect(i), i.body, depth + 1).dim(sp)
        return color
    
    
    

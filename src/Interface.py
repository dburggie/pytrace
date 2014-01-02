from py3D import Vector, Ray, Body

class Interface:
    
    
    
    _distance = None
    _poi = None
    _body = None
    _normal = None
    _color = None
    
    
    
    def __init__(self,
            distance = None,
            poi = None,
            body = None,
            normal = None,
            color = None):
        
        self.distance = distance
        self.poi = poi
        self.body = body
        self.normal = normal
        self.color = color
        if body != None:
            self.matte = body.is_matte
            self.exp = body.exp
        else:
            self.matte = None
            self.exp = None
    
    
    
    def dup(self):
        return Interface(
                self.distance,
                self.poi,
                self.body,
                self.normal,
                self.color)
    
    
    
    def reset(self):
        self.distance = None
        self.poi = None
        self.body = None
        self.normal = None
        self.color = None
        self.exp = None
        self.matte = None
        return self
    
    
    
    def hit(self, body, distance):
        if self.body == None or distance < self.distance:
            self.distance = distance
            self.body = body
        return self
    
    
    
    def register_hit(self, ray):
        if self.body != None and self.distance > 0.0:
            self.poi = ray.follow(self.distance)
            self.normal = self.body.normal(self.poi)
            self.color = self.body.get_color(self.poi)
            self.exp = self.body.exp
            self.matte = self.body.is_matte
        return self
    
    
    

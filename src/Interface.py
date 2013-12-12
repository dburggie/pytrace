from Vector import Vector
from Body import Body

class Interface:
    
    
    
    distance = None
    poi = None
    body = None
    normal = None
    color = None
    
    
    
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
        return self
    
    
    
    def hit(self, body, distance):
        if distance < self.distance or self.body == None:
            self.distance = distance
            self.body = body
        return self
    
    
    
    def register_hit(self, ray):
        if self.body != None and self.distance > 0.0:
            self.poi = ray.follow(self.distance)
            self.normal = self.body.normal(self.poi)
            self.color = self.body.get_color(self.poi)
            print "registered a hit at distance", self.distance
            print "    hit details:"
            print "        poi:    ", self.poi.p()
            print "        normal: ", self.normal.p()
            print "        color:  ", self.color.p()
            print "        body:   ", self.body.p()
        else:
            print "no hit registered: hit the sky."
        return self
    
    
    

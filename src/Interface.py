from Vector import Vector
from Ray import Ray
from Body import Body

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
        
        self._distance = distance
        self._poi = poi
        self._body = body
        self._normal = normal
        self._color = color
    
    
    
    def dup(self):
        return Interface(
                self._distance,
                self._poi,
                self._body,
                self._normal,
                self._color)
    
    
    
    def reset(self):
        self._distance = None
        self._poi = None
        self._body = None
        self._normal = None
        self._color = None
        return self
    
    
    
    def hit(self, body, distance):
        if self._body == None or distance < self._distance:
            self._distance = distance
            self._body = body
        return self
    
    
    
    def register_hit(self, ray):
        if self._body != None and self._distance > 0.0:
            self._poi = ray.follow(self.distance)
            self._normal = self._body.normal(self._poi)
            self._color = self._body.get_color(self._poi)
            print "registered a hit at distance", self.distance
            print "    hit details:"
            print "        poi:    ", self.poi.p()
            print "        normal: ", self.normal.p()
            print "        color:  ", self.color.p()
            print "        body:   ", self.body.p()
        else:
            print "no hit registered: hit the sky."
        return self
    
    
    

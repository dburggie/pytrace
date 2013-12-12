
class Color:
    r = 0.0
    b = 0.0
    g = 0.0
    
    def __init__(self, r = 0.001, b = 0.001, g = 0.001):
        self.r = r
        self.b = b
        self.g = g
    
    def p(self):
        return [max(int(self.r * 256),255),
                max(int(self.b * 256),255),
                max(int(self.g * 256),255)]
    
    def gamma(self, gamma):
        self.r **= gamma
        self.b **= gamma
        self.g **= gamma
        return self
    
    def dup(self):
        return Color(self.r, self.b, self.g)
    
    def set_rbg(self, r, b, g):
        self.r = r
        self.b = b
        self.g = g
        return self
    
    def copy(self, color):
        self.r = color.r
        self.b = color.b
        self.g = color.g
        return self
    
    def dim(self, factor):
        self.r *= factor
        self.b *= factor
        self.g *= factor
        return self
    
    def __add__(self, color):
        self.r += color.r
        self.b += color.b
        self.g += color.g
        return self

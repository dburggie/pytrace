import bounds

class Color:
    r = 0.0
    b = 0.0
    g = 0.0
    
    def __init__(self, r = 0.001, g = 0.001, b = 0.001):
        self.r = r
        self.g = g
        self.b = b
    
    def __eq__(self, c):
        if abs(self.r - c.r) > bounds.small:
            return False
        if abs(self.g - c.g) > bounds.small:
            return False
        if abs(self.b - c.b) > bounds.small:
            return False
        return True
    
    def __add__(self, color):
        self.r += color.r
        self.g += color.g
        self.b += color.b
        return self
    
    def p(self):
        return [min(int(self.r * 256),255),
                min(int(self.g * 256),255),
                min(int(self.b * 256),255)]
    
    def avg(self, color, n):
        a = (n - 1.0) / n
        b = 1.0 / n
        self.r = self.r * a + color.r * b
        self.g = self.g * a + color.g * b
        self.b = self.b * a + color.g * b
        return self
    
    def gamma(self, gamma):
        self.r **= gamma
        self.g **= gamma
        self.b **= gamma
        return self
    
    def dup(self):
        return Color(self.r, self.g, self.b)
    
    def set_rgb(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        return self
    
    def copy(self, color):
        self.r = color.r
        self.g = color.g
        self.b = color.b
        return self
    
    def dim(self, factor):
        self.r *= factor
        self.g *= factor
        self.b *= factor
        return self

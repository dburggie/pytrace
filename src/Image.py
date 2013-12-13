from Color import Color
from pypng import Png

class Image(Png):
    
    width = 0
    height = 0
    scanlines = []
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        Png.__init__(self,width,height)
        self.scanlines = []
        for i in range(height):
            self.scanlines.append([ Color() for i in range(width) ])
    
    def set_pixel(self, x, y, color):
        self.scanlines[y][x] = color
        return self
    
    def get_pixel(self, x, y):
        return self.scanlines[y][x]
    
    def gamma(self, gfactor):
        for lines in self.scanlines:
            for pixels in lines:
                pixels.gamma(gfactor)
        return self
    
    def toPNG(self):
        for y in range(self.height):
            for x in range(self.width):
                Png.set_pixel(self,x,y,self.get_pixel(x,y).p())
        return self

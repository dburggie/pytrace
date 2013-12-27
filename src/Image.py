from py3D import Color
from pypng import Png

class Image(Png):
    
    _i_width = 0
    _i_height = 0
    _scanlines = []
    
    def __init__(self, width, height):
        Png.__init__(self, width, height)
        self._i_width = width
        self._i_height = height
        self._scanlines = []
        for i in range(height):
            self._scanlines.append([ Color() for k in range(width) ])
    
    def set_pixel(self, x, y, color):
        self._scanlines[y][x].copy(color)
        return self
    
    def get_pixel(self, x, y):
        return self._scanlines[y][x]
    
    def gamma(self, gfactor):
        for lines in self._scanlines:
            for pixels in lines:
                pixels.gamma(gfactor)
        return self
    
    def toPNG(self):
        
        for y in range(self._i_height):
            for x in range(self._i_width):
                Png.set_pixel(self,x,y,self.get_pixel(x,y).p())
        return self

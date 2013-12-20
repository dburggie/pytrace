from Vector import Vector
from Ray import Ray
from rand import rand

_default_ppu = 100

class Camera:
    
    
    def set_position(self, v):
        self.o = v
        return self
    
    def set_focus(self, v):
        self.focus = v.norm()
        return self
    
    def set_orientation(self, up):
        self.right = self.focus.cross(up).norm()
        self.up = self.right.cross(self.focus).norm()
        return self
    
    def set_window(self, x, y):
        self.width = x
        self.height = y
        self.d = self.focus.dup()
        self.d.add(self.up, y / 2.0)
        self.d.add(self.right, x / (-2.0))
        return self
    
    def set_ppu(self, ppu = _default_ppu):
        self.ppu = ppu
        self.xstep = self.right.dup().scale(1.0/ppu)
        self.ystep = self.up.dup().scale(-1.0/ppu)
        return self
    
    def _reset(self):
        self.set_window(self.width, self.height)
        self.set_ppu(self.ppu)
        return self
    
    def get_ray(self, x, y):
        o = self.o.dup()
        d = self.d.dup().add(self.xstep, x + rand()).add(self.ystep, y + rand())
        return Ray(o, d)
    
    def __init__(self, origin = Vector(0.0,1.0,0.0),
            focus = Vector(0.0,0.0,1.0),
            width = 2.0, height = 2.0,
            up = Vector(0.0,1.0,0.0) ):
        """Instantiates new object."""
        
        self.r = Ray()
        self.set_position(origin)
        self.set_focus(focus)
        self.set_orientation(up)
        self.set_window(width, height)
        self.set_ppu()
    
    
    

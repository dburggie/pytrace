from py3D import Vector, Ray
from rand import rand

_default_ppu = 100

class Camera:
    
    
    def set_position_delta(self, d):
        if d == None:
            self._delta = None
            return self
        if isinstance(d, float):
            self._delta = d
            return self
        raise d
    
    def set_orientation(self, up):
        self.right = self.forward.cross(up).norm()
        self.up = self.right.cross(self.forward).norm()
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
    
    def set_focus(self, v):
        self.forward = (v - self.o).norm()
        self.focus = v
        if self._init:
            self._reset
        return self
    
    def set_position(self, v):
        self.o = v
        if self._init:
            self.set_focus(self.focus)
            self._reset
        return self
    
    def get_ray(self, x, y):
        o = self.o.dup()
        if self._delta != None:
            o.delta(self._delta)
        d = self.d.dup()
        d.add(self.xstep, x + rand())
        d.add(self.ystep, y + rand())
        d.add(self.o, -1.0).norm()
        return Ray(o, d)
    
    def dup(self):
        c = Camera(self.o, self.focus, self.width, self.height, self.up)
        c.set_ppu(self.ppu)
        c.set_position_delta(self._delta)
        return c
    
    def __init__(self, origin = Vector(0.0,1.0,0.0),
            focus = Vector(0.0,0.0,1.0),
            width = 2.0, height = 2.0,
            up = Vector(0.0,1.0,0.0) ):
        """Instantiates new object."""
        self._init = False
        self.set_position( origin )
        self.set_focus(focus)
        self.set_orientation(up)
        self.set_window(width, height)
        self.set_ppu()
        self.set_position_delta(None)
        self._init = True
    
    
    

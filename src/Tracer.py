from World import World
from Camera import Camera
from Color import Color
from Vector import Vector
from Image import Image

_default_filename = 'trace.png'

class Tracer:
    world = World()
    camera = Camera()
    image = Image(1,1)
    
    def __init__(self, world = None, camera = None):
        self.world = world
        self.camera = camera
        self._drawn = False
        self.image = None
    
    def set_camera(self, camera = Camera()):
        self.camera = camera
        return self
    
    def set_world(self, world = World()):
        self.world = world
        return self
    
    def draw(self, passes = 8):
        if self.world == None:
            self.set_world()
        if self.camera == None:
            self.set_camera()
        ppu = self.camera.ppu
        width = int(ppu * self.camera.width)
        height = int(ppu * self.camera.height)
        self.image = Image(width, height)
        c = Color()
        for y in range(height):
            print 'drawing line', y + 1, 'of', height,
            for x in range(width):
                c.set_rgb(0.0,0.0,0.0)
                for p in range(passes):
                    c = c + self.world.sample(self.camera.get_ray(x,y))
                self.image.set_pixel(x,y,c.dim(1.0 / passes))
            print c.p()
        self._drawn = True
        return self
    
    def write(self, filename = _default_filename):
        if not self._drawn:
            raise self.image
        print 'encoding as {}...'.format(filename),
        self.image.toPNG().write(filename)
        print '        ALL DONE!'
        return self

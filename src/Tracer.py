from Camera import Camera
from Image import Image
from World import World
from py3D import Color, Vector
import time

_default_filename = 'trace.png'

class Tracer:
    _world = World()
    _camera = Camera()
    _image = Image(1,1)
    
    def __init__(self, world = None, camera = None):
        self._world = world
        self._camera = camera
        self._drawn = False
        self._image = None
    
    def set_camera(self, camera = Camera()):
        self._camera = camera
        return self
    
    def set_world(self, world = World()):
        self._world = world
        return self
    
    def draw(self, passes = 8):
        if self._world == None:
            self.set_world()
        if self._camera == None:
            self.set_camera()
        ppu = self._camera.ppu
        width = int(ppu * self._camera.width)
        height = int(ppu * self._camera.height)
        self._image = Image(width, height)
        c = Color()
        t_0 = time.time()
        for y in range(height):
            lt0 = time.time()
            print 'drawing line', y + 1, 'of', height
            for x in range(width):
                c.set_rgb(0.0,0.0,0.0)
                for p in range(passes):
                    c = c + self._world.sample(self._camera.get_ray(x,y))
                self._image.set_pixel(x,y,c.dim(1.0 / passes))
            lt1 = time.time()
            ltime = lt1 - lt0
            ttime = lt1 - t_0
            lleft = height - 1 - y
            mleft1 = ltime * lleft / 60
            mleft2 = ttime / (y + 1) * lleft / 60
            print 'line took {0:.3} seconds.'.format(ltime),
            print '{0:.5} to {1:.5} minutes left'.format(mleft1, mleft2)
        self._drawn = True
        return self
    
    def write(self, filename = _default_filename, gamma = None):
        if not self._drawn:
            raise self._image
        if not gamma == None:
            self._image.gamma(gamma)
        print 'encoding as {}...'.format(filename)
        self._image.toPNG().write(filename)
        print '        ALL DONE!'
        return self

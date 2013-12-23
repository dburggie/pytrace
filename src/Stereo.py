from Camera import Camera
from Image import Image
from World import World
from py3D import Color, Vector

_default_filename = 'trace.png'

class Stereo:
    world = World()
    camera_l = Camera()
    camera_r = Camera()
    image = Image(1,1)
    
    def set_camera(self, camera = Camera()):
        if camera == None:
            camera = Camera()
        crp = camera.o.dup().add(camera.right, 0.1)
        crf = camera.focus.dup().add(camera.right, 0.1)
        clp = camera.o.dup().add(camera.right, -0.1)
        clf = camera.focus.dup().add(camera.right, -0.1)
        self.camera_r = camera.dup().set_focus(crf).set_position(crp)
        self.camera_l = camera.dup().set_focus(clf).set_position(clp)
        return self
    
    def set_world(self, world = World()):
        self.world = world
        return self
    
    def __init__(self, world = None, camera = None):
        self.world = world
        self.set_camera(camera)
        self._drawn = False
        self.image = None
    
    def draw(self, passes = 8):
        if self.world == None:
            self.set_world()
        ppu = self.camera_r.ppu
        w = int(ppu * self.camera_r.width)
        width = 2 * w
        height = int(ppu * self.camera_r.height)
        self.image = Image(width, height)
        c = Color()
        for y in range(height):
            print 'drawing line', y + 1, 'of', height
            for x in range(w):
                # draw pixel from left camera
                c.set_rgb(0.0,0.0,0.0)
                for p in range(passes):
                    c = c + self.world.sample(self.camera_l.get_ray(x,y))
                self.image.set_pixel(x,y,c.dim(1.0 / passes))
                # draw pixel from right camera
                c.set_rgb(0.0,0.0,0.0)
                for p in range(passes):
                    c = c + self.world.sample(self.camera_r.get_ray(x,y))
                self.image.set_pixel(x + w,y,c.dim(1.0 / passes))
                
        self._drawn = True
        return self
    
    def write(self, filename = _default_filename, gamma = None):
        if not self._drawn:
            raise self.image
        if not gamma == None:
            self.image.gamma(gamma)
        print 'encoding as {}...'.format(filename)
        self.image.toPNG().write(filename)
        print '        ALL DONE!'
        return self

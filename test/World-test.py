from raytrace import Vector
from raytrace import Ray
from raytrace import Sphere
from raytrace import hmSphere
from raytrace import Plane
from raytrace import Sky
from raytrace import World
from raytrace import Color
from raytrace import Image

filename = 'sample-06.png'
width = 256
height = width


s = hmSphere(Vector(0.0,1.0,0.0), 1.0,
        Color(0.001,0.99,0.25),
        Vector(10.0,1.0,0.0))
p = Plane(Vector(0.0,1.0,0.0), Vector(0.0,0.0,0.0), Color(0.8,0.1,0.1))



w = World()
w.add_body(s)
w.add_body(p)
w.set_sky(Sky(Vector(1.0,10.0,1.0), Color(0.2,0.2,0.8)))

camera = Vector(0.0,0.8,16.0)
c_dir = Vector(0.0,0.0,-1.0).norm()
c_up = Vector(0.0,1.0,0.0).norm()
c_origin = Vector(-1.5,2.3,0.0) - camera
c_width = 3.0
c_height = 3.0
c_x = c_dir.cross(c_up).scale(c_width / width)
c_y = c_up.dup().scale(-1 * c_height / height)

ray = Ray()
image = Image(width, height)

for y in range(height):
    print 'scanline', y, 'of', height,
    for x in range(width):
        ray.set_origin(camera.dup())
        ray.set_direction(c_origin.dup().add(c_x, x).add(c_y, y))
        image.set_pixel(x,y,w.sample(ray))
    print 'done'

print 'encoding...'
image.toPNG().write(filename)
print 'all done!'
        

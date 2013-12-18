from raytrace import Vector
from raytrace import Ray
from raytrace import Sphere
from raytrace import World
from raytrace import Color
from raytrace import Image

filename = 'sample-01.png'
width = 256
height = width


s = Sphere(Vector(0.0,0.0,0.0), 1.0, Color(0.001,0.99,0.25))

w = World()
w.add_body(s)
w.set_sky(Color(0.001,0.001,0.99))

camera = Vector(0.0,0.0,16.0)
c_dir = Vector(0.0,0.0,-1.0).norm()
c_up = Vector(0.0,1.0,0.0).norm()
c_origin = Vector(-1.5,1.5,0.0) - camera
c_width = 3.0
c_height = 3.0
c_x = c_dir.cross(c_up).scale(c_width / width)
c_y = c_up.dup().scale(-1 * c_height / height)

ray = Ray()
image = Image(width, height)

for y in range(height):
    for x in range(width):
        ray.set_origin(camera.dup())
        ray.set_direction(c_origin.dup().add(c_x, x).add(c_y, y))
        image.set_pixel(x,y,w.sample(ray))

image.toPNG().write(filename)
        

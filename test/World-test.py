from py3D import Vector, Ray, Sphere, hmSphere, Plane, CheckPlane, Color
from pytrace import Sky, World
from pytrace.src.Image import Image
from pytrace.src.rand import rand
from time import time

filename = 'sample-09.png'
width = 400
height = width


s = hmSphere(Vector(0.0,1.0,0.0), 1.0,
        Color(0.001,0.99,0.25),
        Vector(10.0,1.0,0.0))
p = CheckPlane()



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
color = Color()
loops_per_pixel = 16
t_0 = time()
for y in range(height):
    for x in range(width):
        color.set_rgb(0.0,0.0,0.0)
        for k in range(loops_per_pixel):
            ray.set_origin(camera.dup().delta(0.01))
            ray.set_direction(c_origin.dup().add(c_x, x + rand()).add(c_y, y + rand()))
            color = color + w.sample(ray)
        color.dim(1.0/loops_per_pixel)
        image.set_pixel(x,y,color.dup())
    print 'scanline', y, 'done'
    t_1 = time()
    print '    time: {:}'.format(t_1 - t_0)
    print '    left: ~{:}'.format((t_1 - t_0) * (height - 1 - y))
    t_0 = t_1

print 'encoding...'
image.toPNG().write(filename)
print 'all done!'
        

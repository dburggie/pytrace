import py3D
import pytrace
from py3D.bodies.TruncSphere import TruncSphere

filename = 'ft-07.png'
passes = 1
ppu = 25.0
delta = 0.01
V = py3D.Vector

# setup Camera
cam_o = V(0.0,1.0,10.0)
cam_f = V(0.0,1.0,0.0)
cam = pytrace.Camera(cam_o, cam_f, 4.0, 4.0)
cam.set_position_delta(delta)
cam.set_ppu(ppu)


# setup sky
sun = V(3.0,10.0,3.0).norm()
sky = pytrace.Sky(sun, py3D.Color(0.5,0.5,0.99))

# setup mirror
m_c = V(-1.0,1.0,0.0)
mirror = TruncSphere(m_c, 1.0, py3D.Color(0.75,0.001,0.75))
#m_o = (sun - (m_c - cam_o).norm()).norm()
m_o = V(1.0,1.0,1.0)
mirror.set_orientation(m_o)
mirror.set_cosine(0.1)
mirror.set_reflectivity(0.7)

# setup ball
ball = py3D.Sphere(V(1.0,1.0,0.0), 1.0, py3D.Color(0.1,0.8,0.2))
ball.set_matte()

# setup plane
plane = py3D.CheckCircle(5.0).set_reflectivity(0.0)
plane.set_exp(10.0)

# setup World
world = pytrace.World([mirror, ball, plane], sky)

# trace
pytrace.Tracer(world, cam).draw(passes).write(filename)

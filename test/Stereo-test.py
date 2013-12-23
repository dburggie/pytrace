import py3D
from py3D.bodies.ConcCircle import ConcCircle
import pytrace
from pytrace.src.Stereo import Stereo

filename = 'stereo-03.png'
ppu = 100
passes = 2

C = py3D.Color
V = py3D.Vector

s = py3D.Sphere(V(0.0,1.0,0.0),1.0,C(0.5,0.5,0.5))
c = ConcCircle(5.0)

world = pytrace.World([s,c], pytrace.Sky())
world.set_base_brightness(0.4)

cam = pytrace.Camera(V(0.0,1.0,10.0), V(0.0,1.0,0.0), 3.0,3.0)
cam.set_ppu(ppu)
cam.set_position_delta(0.01)

stereo = Stereo(world, cam)
stereo.draw(passes).write(filename)


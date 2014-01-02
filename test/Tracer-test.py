from pytrace import Tracer, World, Camera
from py3D import Vector, Sky
import cProfile

def run():
    sky = Sky(Vector(1.0,0.0,0.0))
    world = World([],sky)
    cam = Camera(Vector(), Vector(1.0,0.0,0.0))
    cam.set_ppu(20)
    Tracer(world, cam).draw(1).write()

cProfile.run('run()')

from raytrace.src.Tracer import Tracer
from raytrace.src.Sky import Sky
from raytrace.src.World import World
from raytrace.src.Camera import Camera
from raytrace.src.Vector import Vector

sky = Sky(Vector(1.0,0.0,0.0))
world = World([],sky)
cam = Camera(Vector(), Vector(1.0,0.0,0.0))

Tracer(world, cam).draw().write()

#!/usr/bin/python2

from py3D import Vector, Ray, Body, Color
from pytrace.src.Interface import Interface
import cProfile

class bodystub(Body):
    
    def __init__(self, center):
        self.center = center.dup()
    def p(self):
        return 'bodystub'
    def get_color(self, point):
        return Color(0.5,0.5,0.5)
    def normal(self, point):
        return Vector(0.0,0.0,1.0)
    def reflectivity(self, point):
        return 0.5
    def intersection(self, ray):
        d = (ray.o - self.center).length()
        if d < 1.0:
            return d
        else:
            return -1.0

ray_origins = [ Vector(-3.0,-2.0,-1.0),
        Vector(-2.0,-1.0,0.0),
        Vector(-1.0,0.0,1.0),
        Vector(0.0,1.0,2.0),
        Vector(1.0,2.0,3.0)]
ray_directions = [ Vector(-3.0,-2.0,-1.0).norm(),
        Vector(-2.0,-1.0,0.0).norm(),
        Vector(-1.0,0.0,1.0).norm(),
        Vector(0.0,1.0,2.0).norm(),
        Vector(1.0,2.0,3.0).norm()]
rays = []
bodies = []
for origins in ray_origins:
    bodies.append(bodystub(origins.dup()))
    for directions in ray_directions:
        rays.append(Ray(origins.dup().delta(0.1),directions.dup()))

i = Interface()
def run():

    for r in rays:
        i.reset()
        for b in bodies:
            d = b.intersection(r)
            if d > 0.0:
                i.hit(b,d)
        i.register_hit(r)
        if i._body == None:
            print "interface didn't register a hit"
        else:
            if i._distance < 0.0:
                print "interface registered hit at negative distance"
            if i._distance > 0.1:
                print "interface didn't catch closest hit"
            if  i._body.p() != 'bodystub':
                print "interface didn't catch body of correct type"
            if not i._normal == Vector(0.0,0.0,1.0):
                print "interface caught wrong surface normal."
            if not i._color == Color(0.5,0.5,0.5):
                print "interface caught wrong surface color."

cProfile.run('run()')


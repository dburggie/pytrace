#!/usr/bin/python2
from raytrace.src.Vector import Vector
from raytrace.src.Ray import Ray

small = 0.00001

zero = Vector(0.0,0.0,0.0)
up = Vector(0.0,1.0,0.0)

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

# test initialization
for o in ray_origins:
    for d in ray_directions:
        ray = Ray(o,d)
        if not ray.o == o:
            print "__init__() method: set origin incorrectly"
        if not ray.d == d:
            print "__init__() method: set direction incorrectly"
        del ray

# test ray equality
bad_ray = Ray(ray_origins[-1], ray_directions[-1])
for o in ray_origins:
    for d in ray_directions:
        ray = Ray(o.dup(),d.dup())
        good_ray = Ray(o.dup(),d.dup())
        if not ray == good_ray:
            print "__eq__() method: evaluates true wrong"
        if ray == bad_ray:
            print "__eq__() method: evaluates false wrong"
        bad_ray.d = d.dup()
    bad_ray.o = o.dup()
        

# test set_origin() method
ray = Ray(zero.dup(), up.dup())
for o in ray_origins:
    ray.set_origin(o)
    if not ray.o == o:
        print "set_origin() method: set bad origin"
del ray

# test set_direction() method
ray = Ray(zero.dup(),up.dup())
for d in ray_directions:
    ray.set_direction(d.dup())
    if not ray.d == d:
        print "set_direction() method: set bad direction"

# test follow() method
distances = [-3,-2,-1,0,1,2,3]
for t in distances:
    for o in ray_origins:
        for d in ray_directions:
            p = Ray(o.dup(),d.dup()).follow(t)
            if not p == o.dup().add(d, t):
                print "follow() method: didn't follow right"

# test reflect() method
for poi in ray_origins:
    ray = Ray(zero.dup(),poi.dup())
    for normal in ray_directions:
        bounce = ray.dup()
        bounce.reflect(poi.dup(), normal.dup())
        o_sine = ray.d.dot(normal)
        r_sine = bounce.d.dot(normal)
        if abs( o_sine + r_sine ) > small:
            print "reflect() method: exit not at same angle to normal"
            print "    poi:   ", o.p()
            print "    normal:", d.p()
            print "    rayout:", bounce.d.p()
            print "    o_sine:", o_sine
            print "    r_sine:", r_sine



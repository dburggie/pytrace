#!/usr/bin/python2
from raytrace.src.Vector import Vector
d = 0.0001
zero = Vector(0.0,0.0,0.0)
up = Vector(0.0,1.0,0.0)
left = Vector(1.0,0.0,0.0)
forward = Vector(0.0,0.0,1.0)

# test __init__() method (and implicitly: length() method)
u = Vector(3.0,4.0,1.0)
dx,dy,dz = u.x - 3.0, u.y - 4.0, u.z - 1.0
if dx > d or dy > d or dz > d:
    print "Constructor: bad coordinates"
    exit()
if abs( u.l - (26.0 ** 0.5) ) > d:
    print "Constructor: bad length"
    exit()
del u

# test __sub__() method
u = Vector(1.5, 2.5, 3.5)
v = Vector(3.5, 2.5, 1.5)
w = u - v
x = Vector( -2.0, 0.0, 2.0 )
if abs((w - x).l) > d:
    print "__sub__ method: incorrect coordinates"
    exit()
if abs( w.l - (8 ** 0.5) ) > d:
    print "__sub__ method: incorrect length."
    exit()
del u
del v
del w
del x

# test dup() method
u = Vector(1.0,2.0,3.0)
v = u.dup()
if (u - v).l > d:
    print "dup() method: bad coordinates"
    exit()
v.x = 4.0
if (u - v).l < 1.0:
    print "dup() method: not a new instance"
    exit()
del u
del v

# test copy() method
u = Vector(1.0,2.0,3.0)
v = Vector()
v.copy(u)
if (u - v).l > d:
    print "copy() method: bad coordinates"
if abs(u.l - v.l) > d:
    print "copy() method: bad length"
del u
del v

# test add() method
u = Vector(-1.0,1.0,3.0)
v = Vector(-2.0,2.0,3.0)
w = Vector()
for s in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    w.copy(u)
    w.add(v, s)
    x = Vector(u.x + s * v.x, u.y + s * v.y, u.z + s * v.z)
    if (w - x).l > d:
        print "add() method: bad coordinates with scalar", s
        exit()
    if abs(w.l - x.l) > d:
        print "add() method: bad length with scalar", s
        exit()
    del x
del s
del u
del v
del w

# test scale() method
u = Vector(1.0,2.0,3.0)
for s in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    v = Vector( s * 1.0, s * 2.0, s * 3.0 )
    w = u.dup().scale(s)
    if (w - v).l > d:
        print "scale() method: bad coordinates with scalar", s
        exit()
    if abs(v.l - abs(s) * w.l) > d:
        print "scale() method: bad length with scalar", s
        exit()
    del v
    del w
del s
del u

# test trans() method
u = Vector(1.0,2.0,3.0)
v = Vector(-1.0,5.0,0.0)
u.trans(-2.0,3.0,-3.0)
if (u - v).l > d:
    print "trans() method: bad coordinates"
    exit()
if abs(u.l - v.l) > d:
    print "trans() method: bad length"
del u
del v

# test norm() method
if abs(zero.dup().norm().l) > d:
    print "norm() method: tried to normalize zero vector"
    exit()
u = Vector(-3.0,0.0,4.0)
v = u.dup().norm()
if abs(v.l - 1.0) > d:
    print "norm() method: didn't normalize to length 1.0"
    exit()
if (v.scale(u.l) - u).l > d:
    print "norm() method: didn't maintain direction"
    exit()
del u
del v

# test dot() method
for v in [up, right,forward]:
    if abs(v.dot(zero)) > d:
        print "dot() method: handles zero vector poorly"
        exit()
for v in [right,forward]:
    if abs(up.dot(v)) > d:
        print "dot() method: handles orthogonal axis vectors poorly"
        exit()
if abs(right.dot(forward)) > d:
    print "dot() method: handles orthogonal axis vectors poorly"
    exit()
u = Vector(2.0,2.0,2.0).norm()
v = Vector(1.0,1.0,-2.0).norm()
if abs(u.dot(v)) > d:
    print "dot() method: handles orthogonal vectors poorly"
    exit()
del u
del v
u = Vector(3.0,-2.0,-5.0)
v = Vector(7.0,-1.0,2.0)
if abs(u.dot(v) - 12.0) > d:
    print "dot() method: bad non-orthogonal dot products"
    exit()
del u
del v

# test cross product
if (left.cross(up) - forward) > d:
    print "cross() method: fails on axis vectors"
    exit()




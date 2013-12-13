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
if abs( u.length() - (26.0 ** 0.5) ) > d:
    print "Constructor: bad length"
del u

# test __sub__() method
u = Vector(1.5, 2.5, 3.5)
v = Vector(3.5, 2.5, 1.5)
w = u - v
x = Vector( -2.0, 0.0, 2.0 )
if abs((w - x).length()) > d:
    print "__sub__ method: incorrect coordinates"
if abs( w.length() - (8 ** 0.5) ) > d:
    print "__sub__ method: incorrect length."
del u,v,w,x

# test __eq__() method
u = Vector()
v = u.dup()
if not u == v:
    print "__eq__() method: not evaluating true correctly"
v.trans(1.0,1.0,1.0)
if u == v:
    print "__eq__() method: not evaluating false correctly"
del u,v

# test dup() method
u = Vector(1.0,2.0,3.0)
v = u.dup()
if (u - v).length() > d:
    print "dup() method: bad coordinates"
v.x = 4.0
if (u - v).length() < 1.0:
    print "dup() method: not a new instance"
del u,v

# test copy() method
u = Vector(1.0,2.0,3.0)
v = Vector()
v.copy(u)
if (u - v).length() > d:
    print "copy() method: bad coordinates"
if abs(u.length() - v.length()) > d:
    print "copy() method: bad length"
del u,v

# test add() method
u = Vector(-1.0,1.0,3.0)
v = Vector(-2.0,2.0,3.0)
w = Vector()
for s in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    w.copy(u)
    w.add(v, s)
    x = Vector(u.x + s * v.x, u.y + s * v.y, u.z + s * v.z)
    if (w - x).length() > d:
        print "add() method: bad coordinates with scalar", s
    if abs(w.length() - x.length()) > d:
        print "add() method: bad length with scalar", s
    del x
del s,u,v,w

# test scale() method
u = Vector(1.0,2.0,3.0)
for s in [-2.0, -1.0, 0.0, 1.0, 2.0]:
    v = Vector( s * 1.0, s * 2.0, s * 3.0 )
    w = u.dup().scale(s)
    if (w - v).length() > d:
        print "scale() method: bad coordinates with scalar", s
    if abs(v.length() - w.length()) > d:
        print "scale() method: bad length with scalar", s
    del v
    del w
del s,u

# test trans() method
u = Vector(1.0,2.0,3.0)
v = Vector(-1.0,5.0,0.0)
u.trans(-2.0,3.0,-3.0)
if (u - v).length() > d:
    print "trans() method: bad coordinates"
if abs(u.length() - v.length()) > d:
    print "trans() method: bad length"
del u,v

# test norm() method
if abs(zero.dup().norm().length()) > d:
    print "norm() method: tried to normalize zero vector"
u = Vector(-3.0,0.0,4.0)
v = u.dup().norm()
if abs(v.length() - 1.0) > d:
    print "norm() method: didn't normalize to length 1.0"
if (v.scale(u.length()) - u).length() > d:
    print "norm() method: didn't maintain direction"
del u,v

# test dot() method
for v in [up, left,forward]:
    if abs(v.dot(zero)) > d:
        print "dot() method: handles zero vector poorly"
for v in [left,forward]:
    if abs(up.dot(v)) > d:
        print "dot() method: handles orthogonal axis vectors poorly"
if abs(left.dot(forward)) > d:
    print "dot() method: handles orthogonal axis vectors poorly"
u = Vector(2.0,2.0,2.0).norm()
v = Vector(1.0,1.0,-2.0).norm()
if abs(u.dot(v)) > d:
    print "dot() method: handles orthogonal vectors poorly"
del u,v
u = Vector(3.0,-2.0,-5.0)
v = Vector(7.0,-1.0,2.0)
if abs(u.dot(v) - 13.0) > d:
    print "dot() method: bad non-orthogonal dot products"
del u,v

# test cross() method
if (left.cross(up) - forward) > d:
    print "cross() method: fails on axis vectors"
u = Vector(1.0,2.0,3.0)
v = Vector(-1.0,3.0,2.0)
w = u.cross(v)
if abs(u.dot(w)) > d or abs(v.dot(w)) > d:
    print "cross() method: result not perpendicular"
    exit()
del u,v,w

# test delta() method
u = Vector(-3.0,-2.0,-1.0)
for translations in range(3):
    for delt in [0.001, 0.01, 0.1, 1.0, 10.0]:
        v = u.dup().delta(delt)
        if abs( (v - u).length() - delt ) > delt:
            print "delta() method: wrong delta distance"
    u.trans(1.0,1.0,1.0)
del u,v




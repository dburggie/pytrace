from raytrace.src.Color import Color

c = Color(0.0001,0.0001,0.0001)
colors = [c.dup()]
for i in range(99):
    colors.append(c.dup().gamma(0.5))
colors2 = colors[:]

# p() method
for c in colors:
    for s in c.p():
        if s < 0 or s > 255:
            print 'p() method: samples are out of bounds'

# dup() method
for c in colors:
    if not c.dup() == c:
        print 'dup() method: result not equal to arg'

# copy() method
tmp = Color()
for c in colors:
    tmp.copy(c)
    if not tmp == c:
        print 'copy() method: not equal to copied color'


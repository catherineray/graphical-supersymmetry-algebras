import colorsys
import itertools
import sys

n = int(sys.argv[1])
bits = list(itertools.product([0, 1], repeat=n))

HSV_tuples = [(x*1.0/n, 0.5, 0.5) for x in range(n+1)]
tuples = map(lambda x: '#%02x%02x%02x' % tuple(map(lambda x: int(x*255), colorsys.hsv_to_rgb(*x))), HSV_tuples)

def diff(a, b):
    difference = 0
    for a0, b0 in zip(a, b):
        difference += a0 != b0
    return difference

def reprtag(t):
    return "".join(str(b) for b in t)

print 'graph cube {'
print '  ranksep=', n/2.0, ';'
print '  fontsize=8;'
seen = set()
for ((a, b), c) in zip(itertools.product(bits, bits), itertools.cycle(tuples)):
    if diff(a, b) == 1 and (b, a) not in seen:
        seen.add((a, b))
        print '  "', reprtag(a), '"',  '--', '"', reprtag(b), '" [color="',  c, '"]'
print '}'

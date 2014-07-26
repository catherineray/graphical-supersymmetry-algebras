# Hypercube Problem

from itertools import chain, combinations

# Create generator set for hypercube of dimension x
def S(x):
 return set(range(0,x)) 

# From http://stackoverflow.com/questions/18035595/powersets-in-python-using-itertools
def powerset(iterable):
 s = list(iterable) 
 return chain.from_iterable(combinations(s, r) for r in range(len(s)+1)) 

# Generate a list of edges given a list of vertices
def edges(verts):
 return set(frozenset([x, y]) for x in verts for y in verts if len(x ^ y) == 1) 

# Run this to generate hypercube of specified number of dimensions
def Qgen(dimensions):
 genSet = S(dimensions) 
 print(genSet) 
 Verts = list(powerset(genSet)) 
 print(Verts) 
 sVerts = set(frozenset(x) for x in Verts) 
 print(sVerts) 
 print(len(sVerts)) 
 Edges = edges(sVerts) 
 print(Edges) 
 print(len(Edges)) 
 return

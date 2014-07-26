
###cube.py
Shiny Graphviz to generate n-dimensional Hamming cubes which falls apart around n=8.
Dependency: <code>sudo apt-get install graphviz</code>

Make them all in one go:
<code>for i in $(seq 1 8); do python cube.py $i > cube${i}.dot && dot -Tsvg cube${i}.dot > cube${i}.svg; done</code>


###altcube.py
This program generates text files containing all unique n-cubes satisfying the properties described. 
This works in an arbitrary number of dimensions and takes a file of the previous dimension as input.



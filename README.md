###altcube.py
This program generates text files containing all unique n-cubes satisfying the properties described. 
This works in an arbitrary number of dimensions and takes a file of the previous dimension as input.


###cube.py
Shiny Graphviz to generate n-dimensional Hamming cubes which falls apart around n=8.

Dependency: <code>sudo apt-get install graphviz</code>

Make them all in one go:

<code>for i in $(seq 1 8); do python cube.py $i > cube${i}.dot && dot -Tsvg cube${i}.dot > cube${i}.svg; done</code>


###generate_hypercube.py
The set-theoretic approach is just a cool way to think about graph generation and allows for matroid theory-inspired intuitions which are more elegant (as least by my perception) than a combinatorics + linear algebra (rank-nullity theorem or similar) approach.


###square.pl
Coded in desperation to test the conjecture for 3 & 4 dimensions.   

<code>helper.scala</code> autogenerated the legal 4cycles.

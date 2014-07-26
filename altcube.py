import string

dimension_start = 3
dimension_end = 4

# loop through the dimensions you care about
# (stored in files, so you don't have to start from scratch each time)
for dimension in range( dimension_start, dimension_end + 1 ):
	
	# initialize lists & dictionaries as empty
	vertices = []
	edges = []
	faces = {}
	
	# create a list of vertices in string binary form (e.g., '1001' = 9 ).
	for vertex_int in range( 2**dimension ):
		vertices.append( bin( vertex_int )[2:].zfill( dimension ) )
	
	# create a list of valid edges in string binary form (e.g., '10011011' = 9,11 ).
	for vertex in vertices:
		for i in range( len( vertex ) ):
			if vertex[i:i+1] == '0':
				edges.append( vertex + vertex[:i] + '1' + vertex[i+1:] )
	
	# create a list of valid edges in string binary form (e.g., '10011011' = 9,11 ).
	# create a list of valid faces as a lookup table of edges.
	for vertex in vertices:
		for i in range( len( vertex ) ):
			if vertex[i:i+1] == '0':
				edges.append( vertex + vertex[:i] + '1' + vertex[i+1:] )
				# create a list of valid faces as a lookup table of edges.
				for j in range( i + 1, len( vertex ) ):
					if not ( vertex + vertex[:i] + '1' + vertex[i+1:] in faces ):
						faces[ vertex + vertex[:i] + '1' + vertex[i+1:] ] = \
							[ vertex + vertex[:i] + '1' + vertex[i+1:], \
							vertex + vertex[:j] + '1' + vertex[j+1:], \
							vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:], \
							vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ]
					if not ( vertex + vertex[:j] + '1' + vertex[j+1:] in faces ):
						faces[ vertex + vertex[:j] + '1' + vertex[j+1:] ] = \
							[ vertex + vertex[:i] + '1' + vertex[i+1:], \
							vertex + vertex[:j] + '1' + vertex[j+1:], \
							vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:], \
							vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ]
					if not ( vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] in faces ):
						faces[ vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ] = \
							[ vertex + vertex[:i] + '1' + vertex[i+1:], \
							vertex + vertex[:j] + '1' + vertex[j+1:], \
							vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:], \
							vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ]
					if not ( vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] in faces ):
						faces[ vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ] = \
							[ vertex + vertex[:i] + '1' + vertex[i+1:], \
							vertex + vertex[:j] + '1' + vertex[j+1:], \
							vertex[:i] + '1' + vertex[i+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:], \
							vertex[:j] + '1' + vertex[j+1:] + vertex[:i] + '1' + vertex[i+1:j] + '1' + vertex[j+1:] ]
	
	# read in the n-1 dimension valid cubes
		cube_small_file = open( 'cube-' + str( dimension - 1 ) + '.txt', 'r' )
		cubes_small = []
		for line in cube_small_file:
			cubes_small.append( line.strip( '\n' ) )
		cube_small_file.close()
	
	# open the n dimension cube file for writing
		cube_big_file = open( 'cube-' + str( dimension ) + '.txt', 'w' )
	
	# open an error file for writing
		cube_error_file = open( 'cube_error.txt', 'w' )
	
	# combine every cube with every other cube
	for cube1_string in cubes_small:
		for cube2_string in cubes_small:
			# read in n-1 dimension cubes
			cube1_list = [ '0' + cube1[:dimension-1] + '0' + cube1[dimension-1:] for cube1 in cube1_string.split( ',' ) ]
			cube2_list = [ '1' + cube2[:dimension-1] + '1' + cube2[dimension-1:] for cube2 in cube2_string.split( ',' ) ]
			# combine cubes the two possible ways
			for binary_value in range( 0, 2 ):
				new_edges = []
				new_edges_track = []
				new_edges_face_order = []
				cube_big_edges = {}
				# add the edges of two n-1 dimension cubes to the edge list for the n cube
				for cube1_edge in cube1_list:
					cube_big_edges[ cube1_edge[:-1] ] = cube1_edge[-1:]
				for cube2_edge in cube2_list:
					cube_big_edges[ cube2_edge[:-1] ] = cube2_edge[-1:]
				# create a list of the new edges
				for edge in edges:
					if not ( edge in cube_big_edges ):
						new_edges.append( edge )
				# initialize one new edge (to 0 or 1 depending on the for loop)
				for edge in new_edges:
					cube_big_edges[ edge ] = str( binary_value )
					break
				# order the list of new edges so that only one edge will be unknown at any time
				new_edges_track = list( new_edges )
				for edge in new_edges:
					face = faces[ edge ]
					for face_edge in face:
						if face_edge in new_edges_track:
							new_edges_track.remove( face_edge )
							new_edges_face_order.append( face_edge )
				# go through the edges in that order, filling in new edges each time
				for edge in new_edges_face_order:
					odd_even_total = 0
					face = faces[ edge ]
					for face_edge in face:
						if face_edge in cube_big_edges:
							odd_even_total = odd_even_total + int( cube_big_edges[ face_edge ] )
					for face_edge in face:
						if not ( face_edge in cube_big_edges ):
							cube_big_edges[ face_edge ] = str( ( odd_even_total + 1 ) % 2 )
				# now that all edge values are filled in, doublecheck that every face is odd (quadruple-check actually -- inefficiently -- because I lookup by edges)
				for edge in edges:
					odd_even_total = 0
					face = faces[ edge ]
					for face_edge in face:
						if face_edge in cube_big_edges:
							odd_even_total = odd_even_total + int( cube_big_edges[ face_edge ] )
					if odd_even_total % 2 == 0:
						cube_error_file.write( 'EVEN FACE ERROR: ' )
						for face_edge in face:
							cube_error_file.write( face_edge + ':' + cube_big_edges[ face_edge ] + ',' )
						cube_error_file.write( '\n' )
						cube_error_file.write( 'CUBE1: ' + ','.join( cube1_list ) + '\n' )
						cube_error_file.write( 'CUBE2: ' + ','.join( cube2_list ) + '\n' )
				
				# output the n-dimensional cube
				cube_big_list = []
				for edge in edges:
					cube_big_list.append( edge + cube_big_edges[ edge ] )
				cube_big_file.write( ','.join( cube_big_list ) + '\n' )
	cube_big_file.close()



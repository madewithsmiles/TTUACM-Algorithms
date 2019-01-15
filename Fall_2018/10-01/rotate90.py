def transpose(M):
	for i in range(len(M)):
		for j in range(i, len(M)):
			M[i][j], M[j][i] = M[j][i], M[i][j]

def print2D(M):
	for i in range(len(M)):
		print(M[i])

# Rotates an NxN matrix M 90 degrees clockwise
def rotate90(M):
	# Get the transpose of the matrix
	transpose(M)

	# Reverse each row
	for i in range(len(M)):
		M[i].reverse()

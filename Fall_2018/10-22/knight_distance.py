# on_board(c) iff c is one of the cells on a 9x9 board
def on_board(c):
	return c[0] in range(1, 9) and c[1] in range(1, 9)

# add(c, v) is a tuple (m, n) that is the vector addition c + v.
def add(c, v):
	return (c[0] + v[0], c[1] + v[1])

# reach_one_move(c) is the set of cells a knight can reach from cell c
def reach_one_move(c):
	moves = {(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)}
	return {add(c, v) for v in moves if on_board(add(c, v))}

# knight_distance(s, e) is the minimum number of moves you need to make to get from cell s to cell e
# on a 9x9 chess board
def knight_distance(s, e):
	c, sqrs = 0, {s}

	while e not in sqrs:
		# sqrs = {m | n in sqrs and m in reach_one_move(n)}
		sqrs = {m for n in sqrs for m in reach_one_move(n)}
		c += 1

	return c



def fib(n, seen = {}):

	seen[1] = 1
	seen[2] = 2
	if n not in seen:
		seen[n] = fib(n-1, seen) + fib(n-2, seen)
	return seen[n]

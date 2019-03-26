package algo

// Fib Solution by Ynigo Reyes
func Fib(n int) int {
	if n <= 1 {
		return n
	}

	return Fib(n-1) + Fib(n-2)
}

// FibMemo Solution by Ynigo Reyes
func FibMemo(n int, memo map[int]int) int {
	if n <= 1 {
		return n
	} else if memo[n] != 0 {
		return memo[n]
	} else {
		memo[n] = FibMemo(n-1, memo) + FibMemo(n-2, memo)
	}

	return memo[n]
}

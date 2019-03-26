package algo

import (
	"testing"
)

func TestFibRecursive(t *testing.T) {
	n := 4
	ans := 3
	res := Fib(n)

	if ans != res {
		t.Errorf("%v does not equal ans: %v\n", res, ans)
	}

	n = 10
	ans = 55
	res = Fib(n)

	if ans != res {
		t.Errorf("%v does not equal ans: %v\n", res, ans)
	}
}

func TestFibMemo(t *testing.T) {
	n := 4
	ans := 3
	memo := make(map[int]int)
	res := FibMemo(n, memo)

	if ans != res {
		t.Errorf("%v does not equal ans: %v\n", res, ans)
	}

	n = 10
	ans = 55
	memo = make(map[int]int)
	res = FibMemo(n, memo)

	if ans != res {
		t.Errorf("%v does not equal ans: %v\n", res, ans)
	}
}

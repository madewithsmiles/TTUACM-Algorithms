package algo

import "testing"

func TestWordSubsets1(t *testing.T) {
	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"e", "o"}

	ans := []string{"facebook", "google", "leetcode"}

	res := WordSubsets(A, B)

	for i, val := range ans {
		if val != res[i] {
			t.Error("sorry bud!")
		}
	}
}

func TestWordSubsets2(t *testing.T) {
	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"l", "e"}

	ans := []string{"apple", "google", "leetcode"}

	res := WordSubsets(A, B)

	for i, val := range ans {
		if val != res[i] {
			t.Error("sorry bud!")
		}
	}
}

func TestWordSubsets3(t *testing.T) {
	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"e", "oo"}

	ans := []string{"facebook", "google"}

	res := WordSubsets(A, B)

	for i, val := range ans {
		if val != res[i] {
			t.Error("sorry bud!")
		}
	}
}

func TestWordSubsets4(t *testing.T) {
	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"lo", "eo"}

	ans := []string{"google", "leetcode"}

	res := WordSubsets(A, B)

	for i, val := range ans {
		if val != res[i] {
			t.Error("sorry bud!")
		}
	}
}

func TestWordSubsets5(t *testing.T) {
	A := []string{"amazon", "apple", "facebook", "google", "leetcode"}
	B := []string{"ec", "oc", "ceo"}

	ans := []string{"facebook", "leetcode"}

	res := WordSubsets(A, B)

	for i, val := range ans {
		if val != res[i] {
			t.Error("sorry bud!")
		}
	}
}

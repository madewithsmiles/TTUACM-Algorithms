package algo

import "testing"

func TestByReference(t *testing.T) {
	testCase := [][]int{
		[]int{1, 1, 0},
		[]int{1, 0, 1},
		[]int{1, 1, 1},
	}

	ans := FlipAndInvertImageByReference(testCase)

	for i := range ans {
		for j := range ans[i] {
			if testCase[i][j] != ans[i][j] {
				t.Errorf("Values do not match %v : %v", testCase[i][j], ans[i][j])
			}
		}
	}
}

func TestByValue(t *testing.T) {
	testCase := [][]int{
		[]int{1, 1, 0},
		[]int{1, 0, 1},
		[]int{1, 1, 1},
	}

	ans := FlipAndInvertImageByValue(testCase)

	for i := range ans {
		for j := range ans[i] {
			if testCase[i][j] != ans[i][j] {
				t.Errorf("Values do not match %v : %v", testCase[i][j], ans[i][j])
			}
		}
	}
}

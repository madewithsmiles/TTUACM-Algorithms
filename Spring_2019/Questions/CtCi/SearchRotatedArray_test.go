package algo

/*
	Solution by: Ynigo Reyes

	This problem teaches you how to break down complex logic
	and not get lost in thought. As you go through this problem
*/

import "testing"

func TestBinarySearchOnRotaedArray(t *testing.T) {
	testCase := []int{5, 6, 7, 8, 0, 1, 2, 3, 4}
	find := 7
	res := SearchRotatedArray(testCase, find)
	ans := 2

	if ans != res {
		t.Errorf("Answer: %v does not equal test: %v", ans, res)
	}
}

func TestBinarySearchOnSortedArray(t *testing.T) {
	testCase := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	find := 7
	res := SearchRotatedArray(testCase, find)
	ans := 7

	if ans != res {
		t.Errorf("Answer: %v does not equal test: %v", ans, res)
	}
}

func TestBinarySearchOnSortedArray2(t *testing.T) {
	testCase := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
	find := 7
	res := SearchRotatedArray(testCase, find)
	ans := 6

	if ans != res {
		t.Errorf("Answer: %v does not equal test: %v", ans, res)
	}
}

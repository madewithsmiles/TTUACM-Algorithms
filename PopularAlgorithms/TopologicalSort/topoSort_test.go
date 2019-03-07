package algo

import (
	"testing"
)

func TestTopoSort(t *testing.T) {
	graph := [][]int{
		[]int{0, 1},
		[]int{0, 2},
		[]int{1, 3},
		[]int{2, 3},
		[]int{3, 4},
	}

	numOfNodes := 5

	sortedNodes := TopoSort(graph, numOfNodes)

	testCase := [][]int{
		[]int{0},
		[]int{1, 2},
		[]int{1, 2},
		[]int{3},
		[]int{4},
	}

	for i, val := range sortedNodes {
		valid := false
		for _, test := range testCase[i] {
			if test == val {
				valid = true
			}
		}

		if !valid {
			t.FailNow()
		}
	}
}

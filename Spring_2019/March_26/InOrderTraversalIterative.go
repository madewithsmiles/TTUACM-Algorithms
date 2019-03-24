package algo

type treeNode struct {
	Val   int
	Left  *treeNode
	Right *treeNode
}

/**
 * InorderTraversal iterative
 * The hard part about this is being able to keep track of current
 * multiple different ways.
 */
func InorderTraversal(root *treeNode) []int {
	stack := []*treeNode{}
	ans := []int{}

	curr := root // Start at the root

	// While the stack is not empty and the curr is not nil
	for (len(stack) != 0) || (curr != nil) {
		// Go all the way left and add all of the nodes
		for curr != nil {
			stack = append(stack, curr)
			curr = curr.Left
		}

		curr, stack = stack[len(stack)-1], stack[:len(stack)-1] // Pop from stack
		ans = append(ans, curr.Val)                             // Read the current and add it to the ans
		curr = curr.Right                                       // Move to current to the right
	}

	return ans
}

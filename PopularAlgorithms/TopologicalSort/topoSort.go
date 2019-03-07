package algo

/*
	Topographical sort is a sort used on Directed Acyclical graphs that will allow
	you to make sure that if you were to start at the node at the top of the stack,
	that you would be able to traverse completely through the graph.

	The algorithm proceeds like so
	1. Have a way to access any node in the graph. In this case, I was given an adjacency list
		 which means that each entry is in [u, v] form where u points to v. I was also given the
		 number of nodes. Here, I used a for loop and a linear search to make sure that I am able
		 to find all edges starting from 0.
	2. Create a `visited` map/set that contains the visited status of all nodes; set to false
	3. Throw into the recursive helper
			a. Mark the current node as visited
			b. Find/Traverse all of the connected children
			c. Keep recurrsing until you find the deepest child
			d. Once you find the deepest child, push to the stack and go back up the call stack
				 (This essentially pushes the elements to the stack in reverse; child THEN parent)
			e. Repeat b until all all paths of the first node are traversed
	4. Go to the next node on your list (Checkout lines 13-15), but only visit if unvisited
	5. Repeat from step 3 until all visited
	6. Reverse the stack and return

	At this point, if you do a BFS starting at the top of the returned stack, you will be able
	to reach every connected node in the graph
*/

// TopoSort topographically sorts a graph
func TopoSort(graph [][]int, numOfNodes int) []int {
	visited := make(map[int]bool)
	ans := []int{}

	for i := 0; i < numOfNodes; i++ {
		visited[i] = false
	}

	// Start Sort
	for i := 0; i < numOfNodes; i++ {
		if visited[i] == false {
			topoSortUtil(i, &visited, &ans, &graph)
		}
	}

	// Reverse the stack
	left, right := 0, len(ans)-1
	for left < right {
		temp := ans[left]
		ans[left] = ans[right]
		ans[right] = temp
		left++
		right--
	}

	return ans
}

// DFS and find the deepest children; Must do it recursively
func topoSortUtil(i int, visited *map[int]bool, stack *[]int, graph *[][]int) {
	(*visited)[i] = true

	q := [][]int{}
	for index, val := range *graph {
		if val[0] == i {
			q = append(q, val)
			(*graph)[index] = []int{-1, -1}
		}
	}

	// For each child (right index), recurse
	for len(q) != 0 {
		curr := q[0]
		q = q[1:]

		if (*visited)[curr[1]] == false {
			topoSortUtil(curr[1], visited, stack, graph)
		}
	}

	*stack = append(*stack, i)
}

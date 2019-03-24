package algo

// SearchRotatedArray will search through a sorted array
func SearchRotatedArray(arr []int, r int) int {
	// Find the sorted section of the array
	// Check if r is in that section
	// If not, go to the otherside

	ans := binarySearch(arr, r, 0, len(arr)-1)
	return ans
}

// Returns the index of the found element
func binarySearch(arr []int, r int, left int, right int) int {
	mid := (left + right) / 2
	ans := -1

	if arr[mid] == r {
		return mid
	} else if left >= right {
		return -1
	} else if checkSide(arr, r, left, right) == 0 {
		ans = binarySearch(arr, r, left, mid-1) // Go left
	} else {
		ans = binarySearch(arr, r, mid+1, right) // Go right
	}

	return ans
}

// 0 = left; not 0 = right
func checkSide(arr []int, r int, left int, right int) int {
	side := 1
	mid := (left + right) / 2

	// Left is sorted
	if arr[0] <= arr[mid] && arr[mid-1] <= arr[mid] {
		// If target is in that range
		if arr[0] <= r && arr[mid-1] >= r {
			side = 0
		}
		// Right is sorted
	} else {
		if arr[len(arr)-1] >= r && arr[mid+1] <= r {
			side = 1
		} else {
			side = 0
		}
	}

	return side
}

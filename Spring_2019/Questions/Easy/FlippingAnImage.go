package algo

// This is an Easy Array's problem that will help people break down the problem
// into smaller problems. This is the best way to structure the code so that
// it is readable and easy to explain. It is also a good problem to practice a new
// language on as it deals with references, arrays and loops

// FlipAndInvertImageByReference reverses and inverts the rows of a 2D array by reference
func FlipAndInvertImageByReference(arr [][]int) [][]int {
	for _, row := range arr {
		reverseByRef(&row)
		invertByRef(&row)
	}

	return arr
}

// FlipAndInvertImageByValue reverses and inverts the rows of a 2D array by reference
func FlipAndInvertImageByValue(arr [][]int) [][]int {
	for index, row := range arr {
		arr[index] = reverseByVal(row)
		arr[index] = invertByVal(row)
	}

	return arr
}

func reverseByRef(arr *[]int) {
	left, right := 0, len(*arr)-1
	for right > left {
		temp := (*arr)[left]
		(*arr)[left] = (*arr)[right]
		(*arr)[right] = temp
		left++
		right--
	}
}

func invertByRef(arr *[]int) {
	for i, val := range *arr {
		if val == 0 {
			(*arr)[i] = 1
		} else {
			(*arr)[i] = 0
		}
	}
}

func reverseByVal(arr []int) []int {
	left, right := 0, len(arr)-1
	for right > left {
		temp := arr[left]
		arr[left] = arr[right]
		arr[right] = temp
		left++
		right--
	}

	return arr
}

func invertByVal(arr []int) []int {
	for i, val := range arr {
		if val == 0 {
			arr[i] = 1
		} else {
			arr[i] = 0
		}
	}

	return arr
}

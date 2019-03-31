package algo

// WordSubsets Solution by Ynigo Reyes
// This works by creating a merged map of B so that
// when we check the character count of a's against
// the merged map
//
// This was the optimal solution found on leetcode.
// Visit https://leetcode.com/problems/word-subsets/solution/
func WordSubsets(A []string, B []string) []string {
	bigCounter := make(map[string]int)
	var ans []string

	for _, word := range B {
		tempCounter := countLetters(word)
		for k, v := range tempCounter {
			if bigCounter[k] < v {
				bigCounter[k] = v
			}
		}
	}

	for _, word := range A {
		letterCount := countLetters(word)
		isSub := true
		for k, v := range bigCounter {
			if letterCount[k] < v {
				isSub = false
			}
		}

		if isSub {
			ans = append(ans, word)
		}
	}

	return ans
}

func countLetters(word string) map[string]int {
	counter := make(map[string]int)
	for _, letter := range word {
		counter[string(letter)]++
	}

	return counter
}

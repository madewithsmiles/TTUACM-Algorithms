package score

import (
	"math"
	"strings"
)

func scoreOfParenthesesUsingStack(parens string) float64 {
	stack := []float64{0}

	for _, val := range parens {
		if strings.Compare(string(val), "(") == 0 {
			stack = append(stack, 0)
		} else {
			x := stack[len(stack)-1]
			stack = stack[0 : len(stack)-1]
			stack[len(stack)-1] += math.Max(float64(2*x), float64(1))
		}
	}

	return stack[0]
}

func scoreOfParenthesesUsingCores(parens string) float64 {
	ans := float64(0)
	bal := float64(0)

	for index, val := range parens {
		if strings.Compare(string(val), "(") == 0 {
			bal++
		} else {
			bal--
			if strings.Compare(string(parens[index-1]), "(") == 0 {
				add := math.Pow(float64(2), bal)
				ans += add
			}
		}
	}

	return ans
}

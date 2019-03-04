package score

import (
	"testing"
)

func TestStack(t *testing.T) {
	testCase := scoreOfParenthesesUsingStack("(()(()))")
	if testCase != 6 {
		t.Errorf("Answer was 6; got %v", testCase)
	}
}

func TestCore(t *testing.T) {
	testCase := scoreOfParenthesesUsingCores("(()(()))")
	if testCase != 6 {
		t.Errorf("Answer was 6; got %v", testCase)
	}
}

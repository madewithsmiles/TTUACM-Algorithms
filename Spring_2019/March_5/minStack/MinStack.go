package algo

import (
	"errors"
)

// MinStack a stack that will keep track of the min element
type MinStack struct {
	items    []int
	minItems []int
}

// Pop gets the top of the stack and deletes the min if we pop off a min
func (s *MinStack) Pop() (int, error) {
	if s.IsEmpty(s.items) {
		return 0, errors.New("Nothing to pop")
	} else if s.peek(s.items) == s.peek(s.minItems) {
		copy(s.minItems, s.minItems[:len(s.minItems)-1])
	}

	val := s.peek(s.items)

	copy(s.items, s.items[:len(s.items)-1])

	return val, nil
}

// Min gets the minimum item in the stack
func (s *MinStack) Min() int {
	return s.peek(s.minItems)
}

// Push pushes an item to the stack and to the min stack if it is the new min
func (s *MinStack) Push(val int) {
	if s.IsEmpty(s.minItems) {
		s.minItems = append(s.minItems, val)
	} else if val < s.peek(s.minItems) {
		s.minItems = append(s.minItems, val)
	}
	s.items = append(s.items, val)
}

// IsEmpty checks if given array is empty
func (s *MinStack) IsEmpty(arr []int) bool {
	return len(arr) == 0
}

func (s *MinStack) peek(arr []int) int {
	return arr[len(arr)-1]
}

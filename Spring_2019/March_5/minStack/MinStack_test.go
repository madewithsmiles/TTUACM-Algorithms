package algo

import "testing"

func TestDoubleMinStack(t *testing.T) {
	var stack MinStack

	stack.Push(3)
	stack.Push(5)
	stack.Push(-1)
	stack.Push(6)
	stack.Push(100)
	stack.Push(0)

	if stack.Min() != -1 {
		t.Errorf("Min does not function correctly. Expected -1, not %v", stack.Min())
	}

	top, err := stack.Pop()
	if err != nil {
		t.Errorf("wat: %v", err)
	}

	if top != 0 {
		t.Errorf("Pop or Push does not function correctly. Expected 0, not %v", top)
	}
}

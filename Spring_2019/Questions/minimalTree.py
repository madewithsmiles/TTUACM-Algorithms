import unittest

class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

def minimalBST(arr, left, right):
    if right < left:
        return None

    mid = (left + right) // 2

    head = Node(arr[mid])
    head.left = minimalBST(arr, left, mid - 1)
    head.right = minimalBST(arr, mid + 1, right)

    return head

class Test(unittest.TestCase):
    def testSortedArrayWithAnswer(self):
        case = [1, 2, 3, 4, 5, 6, 7]
        tree = minimalBST(case, 0, len(case) - 1)
        self.assertEqual(tree.val, 4, "head value is not correct")
        self.assertEqual(tree.left.val, 2)
        self.assertEqual(tree.left.left.val, 1)
        self.assertEqual(tree.left.right.val, 3)

        self.assertEqual(tree.right.val, 6)
        self.assertEqual(tree.right.left.val, 5)
        self.assertEqual(tree.right.right.val, 7)

if __name__ == "__main__":
    unittest.main()

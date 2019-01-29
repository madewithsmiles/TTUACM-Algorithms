import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(unittest.TestCase):
    @staticmethod
    def insertIntoBST(root, val):
        curr = root
        inserted = False
        while not inserted:
            if val > curr.val and curr.right:
                curr = curr.right
            elif val > curr.val:
                curr.right = TreeNode(val)
                inserted = True
            elif val < curr.val and curr.left:
                curr = curr.left
            elif val < curr.val:
                curr.left = TreeNode(val)
                inserted = True

        return root

    def testInsertion(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)

        val = 5

        tree = self.insertIntoBST(root, val)

        self.assertEqual(True, self.checkIfValidTreeAndValueInside(tree, val))

    @staticmethod
    def checkIfValidTreeAndValueInside(tree, val):
        q = [tree]
        containsVal = False

        while q:
            curr = q.pop(0)

            if curr.val == val:
                containsVal = True
            if curr.left:
                if curr.left.val > curr.val: return False
                q.append(curr.left)
            if curr.right:
                if curr.right.val < curr.val: return False
                q.append(curr.right)

        return containsVal

if __name__ == '__main__':
    unittest.main()

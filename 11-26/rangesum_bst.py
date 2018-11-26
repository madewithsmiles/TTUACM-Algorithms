from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        
        # Keep track of total
        total = 0
        
        if not root: 
            return
      
        # Create a deque with the root in it 
        queue = deque(root)
        
        # Level order traversal
        while queue: 
            
            node = queue.popleft()
            
            if L <= node.val <= R:
                total += node.val

            if node.left: 
                queue.append(node.left) 

            if node.right: 
                queue.append(node.right) 
        
        return total

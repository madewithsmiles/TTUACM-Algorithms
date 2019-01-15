# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        # Initialize head to None 
        head = None
        
        # The merge of l1 and an empty list is l1, and vice versa
        if not l1: return l2
        if not l2: return l1
        
        # If l1.val belongs before l2.val in the final list
        if l1.val <= l2.val:
            # Our new head is l1 since l1 will come before l2
            head = l1
            # The rest of the list will be the merged list of l1.next and l2
            # We progress l1 because we just kept its head node back as the head
            # We keep l2 the same because we are still searching for a place to put its head node
            head.next = self.mergeTwoLists(l1.next, l2)
        # If l2.val belongs before l1.val
        else:
            # Our new head is l2 since l2 will come before l1
            head = l2
            # The rest of the list will be the merged list of l1 and l2.next
            # We keep l1 the same since we are still searching for a place to put its head node
            # We progress l2 because we just kept its head node back
            head.next = self.mergeTwoLists(l1, l2.next)
        
        return head
        

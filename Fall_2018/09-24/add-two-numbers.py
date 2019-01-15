# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        # Keep track of the sum of the two numbers
        total = 0
        # Keep track of the index we were on
        i = 0
        
        # Progress while at least one of the lists is valid
        while l1 or l2:
            # Only progress if the list is valid
            if l1:
                # The value * 10^i gives you the number to add to total, for example
                # List: 1 - > 2
                # Total = 1*10^0 + 2*10^1 = 21 which is that number in integer form
                total += l1.val * pow(10, i)
                l1 = l1.next
            if l2:
                total += l2.val * pow(10, i)
                l2 = l2.next
            i += 1
        
        # Create the head of our new list we are constructing as the ones digit
        cur = ListNode(total % 10)
        # Chop off the last digit, the one we just added
        total = total // 10
        
        # Save the head so we can return it
        head = cur
        
        # If the total is 0 then we have no number left to process
        while total != 0:
            # Repeat process above, add last digit of total as a node, and then chop off the last digit
            cur.next = ListNode(total % 10)
            total = total // 10
            cur = cur.next
        
        return head


# Time complexity: O(n)
# Space complexity: O(n)

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        ret = []
        for e in A:
            if e % 2 == 0:
                ret.insert(0, e)
            else:
                ret += [e]
        
        return ret

# Time complexity: O(n)
# Space complexity: O(1)
class Solution(object):
    def sortArrayByParity(self, A):
       
        i = 0
        j = len(A) - 1
        
        while i < j:
            
            if A[i] % 2 == 1 and A[j] % 2 == 0:
                A[i],A[j] = A[j],A[i]
            
            if A[i] % 2 == 0: i += 1
            if A[j] % 2 == 1: j -= 1
        
        return A

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

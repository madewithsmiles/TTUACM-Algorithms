from typing import Dict, List
from collections import namedtuple
import unittest

class Solution(unittest.TestCase):
    def test(self):
        testcase = namedtuple('testcase','A B Output')
        
        A_ = ["amazon","apple","facebook","google","leetcode"]
        testcases = []
        
        testcases.append(testcase(A=A_, B=["e","o"], Output=["facebook","google","leetcode"]))
        testcases.append(testcase(A=A_, B=["l","e"], Output=["apple","google","leetcode"]))
        testcases.append(testcase(A=A_, B=["e","oo"], Output=["facebook","google"]))
        testcases.append(testcase(A=A_, B=["lo","eo"], Output=["google","leetcode"]))
        testcases.append(testcase(A=A_, B=["ec","oc","ceo"], Output=["facebook","leetcode"]))

        for tstcase in testcases:
            self.assertListEqual(tstcase.Output, self.wordSubsets(tstcase.A, tstcase.B))

    def charCounter(self, s: str) -> Dict[str, int]:
        res = {}

        for ch in s:
            if ch not in res:
                res[ch] = 1
            else:
                res[ch] += 1
        
        return res
    
    def wordSubsets(self,A: List[str], B: List[str]) -> List[str]:
        res = []
        
        # Sanity check
        if len(A) == 0 or len(B) == 0:
            return res
        
        # "Merging" b
        new_b = {}
        word_char_count = {}
        
        for word in B:
            word_char_count = self.charCounter(word)
    
            for k in word_char_count:
                if k not in new_b or new_b[k] < word_char_count[k]:
                    new_b[k] = word_char_count[k]
            
            word_char_count = {}
        
        # Solve
        for word in A:
            word_char_count = self.charCounter(word)
            is_universal = True
            
            for k in new_b:
                if k not in word_char_count or word_char_count[k] < new_b[k]:
                    is_universal = False
                    break
            
            if is_universal:
                res.append(word)
                
            word_char_count = {}
        
        return res

if __name__ == '__main__':
    unittest.main()
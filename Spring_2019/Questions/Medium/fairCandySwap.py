import unittest

class Solution(unittest.TestCase):
    @staticmethod
    def fairCandySwap(A, B):
        """
        This is a good example of how math would help you in interview questions.
        This is also a good example of how you can use sets and arrays
        Approach this as you would 2 sum and build an equation
        """
        sizeA, sizeB = sum(A), sum(B)
        setB = set(B)
        for el in A:
            target = el + (sizeB - sizeA) // 2
            if target in setB:
                return [el, target]

    def testUsingASetAndArray(self):
        A = [1, 1]
        B = [2, 2]

        ans = [1, 2]

        case = self.fairCandySwap(A, B)

        self.assertEqual(case, ans)

    def testUsingASetAndArray2(self):
        A = [1,2,5]
        B = [2,4]

        ans = [5, 4]

        case = self.fairCandySwap(A, B)

        self.assertEqual(case, ans)

if __name__ == '__main__':
    unittest.main()


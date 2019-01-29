import unittest

class Solution(unittest.TestCase):
    @staticmethod
    def sortedSquares(arr):
        """
        This problem will help you understand how to manually sort an array
        and learn important Array(List) methods
        """
        less = []
        zero = []
        more = []

        for el in arr:
            if el < 0:
                less.append(el * el)
            elif el > 0:
                more.append(el * el)
            else:
                zero.append(0)

        ans = []

        while less or more:
            if not more:
                ans.append(less.pop())
            elif not less:
                ans.append(more.pop(0))
            elif less[-1] > more[0]:
                ans.append(more.pop(0))
            elif less[-1] <= more[0]:
                ans.append(less.pop())

        return zero + ans

    def testManualSolution(self):
        arr = [-7, -3, 0, 1, 4, 8]
        case = self.sortedSquares(arr)
        ans = [0, 1, 9, 16, 49, 64]
        self.assertEqual(case, ans)

    def testCaseWithDuplicates(self):
        arr = [-8, -7, -3, 0, 0, 1, 1, 4, 8]
        case = self.sortedSquares(arr)
        ans = [0, 0, 1, 1, 9, 16, 49, 64, 64]
        self.assertEqual(case, ans)

if __name__ == '__main__':
    unittest.main()

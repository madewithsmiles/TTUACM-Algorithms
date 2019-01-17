import unittest

class Test(unittest.TestCase):
    def testSolutionUsingHashTable(self):
        A = [-1,1,1,1,-1]
        B = [0,-1,-1,0,1]
        C = [-1,-1,1,-1,-1]
        D = [0,1,0,-1,-1]

        ans = self.fourSumCount(A, B, C, D)
        self.assertEqual(ans, 132)

    @staticmethod
    def fourSumCount(A, B, C, D):
        """
        LeetCode:
        Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
        there are such that A[i] + B[j] + C[k] + D[l] is zero.

        To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500.
        All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
        """

        ans = 0

        ABsum = dict()

        for a in A:
            for b in B:
                if not ABsum.get(a + b):
                    ABsum[a + b] = 1
                else:
                    ABsum[a + b] += 1

        for c in C:
            for d in D:
                if ABsum.get(-1 * (c + d)):
                    ans += ABsum.get(-1 * (c + d))

        return ans

if __name__ == "__main__":
    unittest.main()

import unittest

class Test(unittest.TestCase):
    def count_steps(self, stairs, memo):
        """
        count_steps

        How many ways are there to climb a n-height staircase
        if you go up in 1, 2, 3 step intervals
        """
        if stairs < 0:
            return 0

        if stairs == 0:
            return 1

        if memo[stairs] > -1:
            return memo[stairs]

        memo[stairs] = self.count_steps(stairs - 1, memo) + self.count_steps(stairs - 2, memo) + self.count_steps(stairs - 3, memo)

        return memo[stairs]

    def testEvenPositiveNumbers(self):
        stairs = 3
        memo = [-1] * (stairs + 1)
        self.assertEqual(self.count_steps(stairs, memo), 4)
    def testOddPositiveNumbers(self):
        stairs = 7
        memo = [-1] * (stairs + 1)
        self.assertEqual(self.count_steps(stairs, memo), 44)

if __name__ == "__main__":
    unittest.main()

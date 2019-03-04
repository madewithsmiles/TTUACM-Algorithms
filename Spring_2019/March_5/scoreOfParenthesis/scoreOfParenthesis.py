import unittest

class Solution(unittest.TestCase):
    @staticmethod
    def scoreOfParenthesesUsingStack(S):
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

    @staticmethod
    def scoreOfParenthesesUsingCores(S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i-1] == '(':
                    ans += 1 << bal
        return ans

    def testStack(self):
        testCase = '(()(()))'
        ans = 6
        self.assertEqual(self.scoreOfParenthesesUsingStack(testCase), ans)

    def testCountingCores(self):
        testCase = '(()(()))'
        ans = 6
        self.assertEqual(self.scoreOfParenthesesUsingCores(testCase), ans)

if __name__ == '__main__':
    unittest.main()

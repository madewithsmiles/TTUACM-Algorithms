import unittest

class Solution(unittest.TestCase):
    @staticmethod
    def isValid(s):
        stack = []
        mapping = {
            "}": "{",
            "]": "[",
            ")": "(",
        }

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

    def testUsingAStack(self):
        testCase = self.isValid('()()')
        self.assertEqual(testCase, True, "Supposed to be True")
        testCase = self.isValid('()(')
        self.assertEqual(testCase, False, "Supposed to be False")

if __name__ == '__main__':
    unittest.main()

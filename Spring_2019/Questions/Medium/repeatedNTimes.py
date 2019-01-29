import unittest

class Test(unittest.TestCase):
    def testIfYouCanFindTheAnswer(self):
        case = [1, 2, 3, 3]
        ans = self.repeatedNTimes(case)
        self.assertEqual(ans, 3)

    @staticmethod
    def repeatedNTimes(arr):
        """
        Leetcode:
        In a array arr of size 2N, there are N+1 unique elements,
        and exactly one of these elements is repeated N times.

        Return the element repeated N times.
        """
        counter = dict()

        n = len(arr) // 2

        for num in arr:
            if not counter.get(num):
                counter[num] = 1
            else:
                counter[num] += 1

        for key, val in counter.items():
            if val == n:
                return key

        return None

if __name__ == "__main__":
    unittest.main()

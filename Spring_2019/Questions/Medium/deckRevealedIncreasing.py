import unittest
import collections

class Solution(unittest.TestCase):
    @staticmethod
    def deckRevealedIncreasing(deck):
        N = len(deck)
        index = collections.deque(range(N))
        ans = [None] * N

        for card in sorted(deck):
            print(card, index)
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans

    def testIntuition(self):
        arr = [17, 13, 11, 2, 3, 5, 7]
        ans = [2,13,3,11,5,17,7]

        case = self.deckRevealedIncreasing(arr)
        self.assertEqual(case, ans)

if __name__ == '__main__':
    unittest.main()

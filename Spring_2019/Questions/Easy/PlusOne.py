class Solution:
    def plusOne(self, digits):
        multiplier = 1
        ans = 1 # Plus One

        # 127 == 100 + 20 + 7
        
        for i in reversed(digits): # Grab the least significant bit
            ans += (i * multiplier) # Start multiplying
            multiplier *= 10           # Each time we iterate, we increase our multiplier
        
        return list(map(int, str(ans)))

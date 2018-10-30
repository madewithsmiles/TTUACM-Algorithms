def missingNumber(self, nums):
"""
:type nums: List[int]
:rtype: int
"""
maxVal = len(nums)

# This works because the underlying data structure for this set is a hashtable,
# which has an 0(1) look up time
hashSet = set(nums)

for element in range(len(nums) + 1):
  if element not in hashSet:
    return element

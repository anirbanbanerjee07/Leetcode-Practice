class Solution(object):
    def twoSum(self, nums, target):
        numToIndex = {}

        for i, num in enumerate(nums):
          if target - num in numToIndex:
            return numToIndex[target - num], i
          numToIndex[num] = i
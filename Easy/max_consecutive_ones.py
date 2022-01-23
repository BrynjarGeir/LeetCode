class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0; i = 0; n = len(nums)
        while i < n:
            if nums[i] == 1:
                j = i
                while j < n and nums[j] == 1:
                    j += 1
                maxones = max(j-i, maxones)
                i = j
            else: i += 1
        return maxones
                    
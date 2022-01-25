class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1: return nums
        nums = sorted(nums, reverse = True); i = 1
        while i < len(nums):
            if sum(nums[:i]) > sum(nums[i:]):
                return nums[:i]
            i += 1
        return nums
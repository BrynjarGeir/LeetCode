class Solution:
    def minOperations(self, nums: List[int]) -> int:
        steps = 0
        for i in range(1,len(nums)):
            if nums[i-1] >= nums[i]:
                step = nums[i-1] - nums[i] + 1
                nums[i] += step
                steps += step
        return steps
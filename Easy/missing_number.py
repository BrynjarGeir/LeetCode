class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort(); n = len(nums)
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1] - 1:
                return nums[i] + 1
        if n in nums: return 0
        return n
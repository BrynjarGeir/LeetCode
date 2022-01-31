class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums: return 1
        
        i, ans = 0, len(nums) + 1
        for j in range(len(nums)):
            target -= nums[j]
            while target <= 0:
                ans = min(ans, j - i + 1)
                target += nums[i]
                i += 1
        return ans % (len(nums) + 1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        n = len(nums)
        ans1 = self.robHouse(nums[:n-1])
        ans2 = self.robHouse(nums[1:])
        
        return max(ans1, ans2)
    
    def robHouse(self, nums):
        prev, curr = 0, 0
        for num in nums:
            v = max(curr, prev + num)
            prev = curr
            curr = v
        return curr
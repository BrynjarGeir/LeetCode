class Solution:
    def getMaximumGenerated(self, n: int) -> int:    
        def generateArray(i, nums):
            while i <= n:
                if i == 0: nums.append(0)
                elif i == 1: nums.append(1)
                elif i % 2 == 0 and i > 0 and i <= n:
                    nums.append(nums[i//2])
                elif not i%2 == 0 and i <= n:
                    nums.append(nums[i//2] + nums[i//2+1])
                i += 1
            return nums
        
        nums = []; i = 0
        nums = generateArray(i, nums)
        return max(nums)
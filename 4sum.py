from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int  ) -> List[List[int]]:
        nums.sort(); sumsToTarget = set(); n = len(nums); i = 0; 
        while i < n:
            j = i+1
            while j < n:
                l, r = j+1, n-1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        sumsToTarget.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1; r -= 1
                    elif nums[l] + nums[r] > remain: r -= 1
                    else: l += 1
                j += 1
            i += 1  
        return sumsToTarget
        
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort(); sumsTo0 = []; n = len(nums); i = 0
        while i < n:
            if nums[i] > 0: break
            j = i + 1; k = n - 1
            while j < k:
                sum3 = nums[i] + nums[j] + nums[k]
                if sum3 == 0:
                    sumsTo0.append([nums[i], nums[j], nums[k]])
                    while j+1 < n and nums[j+1] == nums[j]: j+=1
                    j += 1; k -= 1
                elif sum3 < 0: j += 1
                else: k -= 1
            while i+1 < n and nums[i+1] == nums[i]: i+= 1
            i += 1         
        return sumsTo0
        
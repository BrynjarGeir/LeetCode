from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums); 
        return self.indTwoSum(nums, 0, len(nums) - 1, target)
    def indTwoSum(self, nums: List[int], ind1: int, ind2: int, target: int) -> List[int]:
        if nums[ind1] + nums[ind2] == target: return [ind1, ind2]
        elif nums[ind1] + nums[ind2] > target: return self.indTwoSum(nums, ind1, ind2-1, target)
        else: return self.indTwoSums(nums, ind1+1, ind2, target)
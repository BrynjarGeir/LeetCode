from typing import List
from math import inf
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort(); distance = inf; closest = None
        for i in range(len(nums)-2):
            j, k = i + 1, len(nums)-1
            while j < k:
                value = nums[i] + nums[j] + nums[k]
                if value == target: return value
                elif value > target: k -= 1
                else: j += 1
                currDist = abs(value - target)
                if currDist < distance:
                    distance = currDist; closest = value
        return closest
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while True:
            if len(nums) <= i: break
            if nums[i] == val:
                nums.pop(i); continue
            i += 1
        return len(nums)
        
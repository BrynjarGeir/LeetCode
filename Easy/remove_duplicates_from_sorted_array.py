from collections import deque
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = set(); indexes = deque()
        for i in range(len(nums)):
            if nums[i] in a:
                indexes.appendleft(i)
            else: a.add(nums[i])
        while indexes:
            nums.pop(indexes.popleft())
        return len(nums)

from collections import deque
# This one uses less memory and I think is more in line with what is expected
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while True:
            if len(nums) <= i: break
            if nums[i] in nums[:i]:
                nums.pop(i)
                continue
            i += 1
        return len(nums)
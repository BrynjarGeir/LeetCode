from collections import deque
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        nums = deque(nums); ans = []
        while nums:
            freq = nums.popleft()
            val = nums.popleft()
            ans += [val]*freq
        return ans
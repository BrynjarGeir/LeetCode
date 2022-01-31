class Solution:
    def rob(self, nums: List[int]) -> int:
        prevp, prev, curr = 0,0,0
        for num in nums:
            curr = max(prev, prevp + num)
            prevp = prev
            prev = curr
        return curr
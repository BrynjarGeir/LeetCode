class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        curr = set(nums)
        if len(curr) < 3: return max(nums)
        curr = list(curr)
        curr.sort()
        return curr[-3]
        
        
        
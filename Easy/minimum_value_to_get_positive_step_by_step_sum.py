class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = [0]
        for num in nums:
            total.append(total[-1] + num)
        ans = min(total)
        if ans >= 0: return 1
        else: return -ans+1
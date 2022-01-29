from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []; n = len(nums)
        for i in range(n+1):
            ans += list(combinations(nums, i))
        return ans
from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        if n > 45 or n < k: return []
        
        combs = combinations(range(1,10), k)
        ans = []
        for comb in combs:
            print(comb)
            if sum(comb) == n:
                ans.append(comb)
        
        return ans
        
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = []; counter = Counter(arr)
        for a in arr:
            if a == counter[a]:
                ans.append(a)
        if len(ans) == 0: return -1
        ans = sorted(ans, reverse=True)
        return ans[0]
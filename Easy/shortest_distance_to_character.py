class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexes = [i for i,x in enumerate(s) if x == c]
        ans = [10**4]*len(s); curr = 0
        for i in range(len(s)):
            if s[i] == c:
                ans[i] = 0
                curr += 1
            else:
                if curr == 0:
                    ans[i] = indexes[curr] - i
                else:
                    if curr == len(indexes): ans[i] = i - indexes[curr-1]
                    else:
                        right = indexes[curr]; left = indexes[curr-1]
                        ans[i] = min(right - i, i - left)
        return ans
            
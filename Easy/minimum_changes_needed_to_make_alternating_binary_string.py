class Solution:
    def minOperations(self, s: str) -> int:
        ans = sum(i%2 == int(c) for i,c in enumerate(s))
        return min(ans, len(s)-ans)
class Solution:
    def modifyString(self, s: str) -> str:
        ans, q = '', '?'
        for i,c in enumerate(s):
            nxt = s[i+1] if i + 1 < len(s) else '?'
            q = c if c != '?' else {'a', 'b', 'c'}.difference({q,nxt}).pop()
            ans += q
        return ans
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        m, n = len(s), len(p)
        i = j = 0
        last_i, last_j = 0, -1
        while i < m:
            if j < n and (p[j] == '?' or p[j] == s[i]):
                i += 1; j += 1
            elif j < n and p[j] == '*':
                last_i = i; last_j = j
                j += 1
            elif last_j >= 0:
                i = last_i + 1
                last_i += 1
                j = last_j
            else: return False
        while j < n and p[j] == '*':
            j += 1
        return j == n
                
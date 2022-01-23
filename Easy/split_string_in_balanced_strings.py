class Solution:
    def balancedStringSplit(self, s: str) -> int:
        if len(s) < 4: return False
        ans = []; ind = 2
        while s:
            if s[:ind].count('L') == s[:ind].count('R') and s[ind:].count('L') == s[ind:].count('R'):
                ans.append(s[:ind])
                s = s[ind:]
                ind = 2
            else: ind += 1
        return len(ans)
            
            
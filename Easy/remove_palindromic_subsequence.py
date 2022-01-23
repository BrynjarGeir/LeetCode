class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalindrome(s):
            n = len(s)//2
            if len(s) % 2 == 0:
                return s[:n] == s[n:][::-1]
            else: return s[:n] == s[n+1:][::-1]
        if not s: return 0
        if isPalindrome(s): return 1
        return 2
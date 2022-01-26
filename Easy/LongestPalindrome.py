class Solution:
    def longestPalindrome(self, s: str) -> str:
        longestPal = ''
        for i in range(len(s)):
            length = len(longestPal)
            for j in range(i,len(s), length-1):
                curr = s[i:j+1]
                if self.isPalindrome(curr) and len(curr) > len(longestPal):
                    longestPal = curr
        return longestPal
                    

    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1: return True
        elif len(s)%2 == 0:
            first = [c for c in s[:int(len(s)/2)]]
            second = list(reversed([c for c in s[int(len(s)/2):]]))
        else:
            first = [c for c in s[:int(len(s)/2)]]
            second = list(reversed([c for c in s[int(len(s)/2) + 1:]]))
        return first == second
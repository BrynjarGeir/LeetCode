class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '': return 0
        jump = len(needle)
        for i in range(len(haystack)-jump+1):
            if haystack[i:i+jump] == needle:
                return i
        return -1
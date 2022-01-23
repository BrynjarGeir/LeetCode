class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0; sb = ''
        for c in s:
            if c not in sb:
                sb += c
            else:
                sb = sb[sb.index(c) + 1 :] + c
            maximum = max(maximum, len(sb))
        return maximum
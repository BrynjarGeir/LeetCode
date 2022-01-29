from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = Counter(s); n = len(s) - 1
        if max(count.values()) < 2: return -1
        
        longest = 0; s = list(s)
        
        for i in range(len(s)):
            if s[i] in s[i+1:]:
                curr = s[i+1:][::-1]
                dist = n - curr.index(s[i]) - i - 1
                longest = max(longest, dist)
        return longest
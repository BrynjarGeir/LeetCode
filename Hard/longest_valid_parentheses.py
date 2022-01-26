from collections import deque
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 1 or s == '': return 0
        opened = deque()
        for i,p in enumerate(s):
            if p == '(': opened.append(i)
            else:
                if opened:
                    if s[opened[-1]] == '(': opened.pop()
                    else: opened.append(i)
                else:
                    opened.append(i)
        if not opened: return len(s)
        else:
            longest = 0
            a, b = len(s), 0
            while opened:
                b = opened.pop()
                longest = max(longest, a-b-1)
                a = b
            longest = max(longest, a)
            return longest
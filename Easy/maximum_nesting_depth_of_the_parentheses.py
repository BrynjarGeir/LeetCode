from collections import deque
class Solution:
    def maxDepth(self, s: str) -> int:
        if not s or (len(s) == 1 and s != '(' and s != ')'): return 0
        opened = deque()
        maxdepth = 0; depth = 0
        for c in s:
            if c == '(':
                opened.append(c)
                depth += 1
            if c == ')':
                try:
                    opened.pop()
                    maxdepth = max(maxdepth, depth)
                    depth -= 1
                except:
                    continue
            else:
                continue
        return maxdepth
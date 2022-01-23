from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        if not set(s).issubset(set(t)): return False
        s = deque(s); t = deque(t); ind = 0
        while s and ind < len(t):
            if s[0] == t[ind]:
                s.popleft()
            ind += 1
        if not s: return True
        return False
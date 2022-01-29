class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or sorted(s) != sorted(goal): return False
        
        for i in range(len(s)):
            if s[i:] + s[:i] == goal: return True
            if s[-i:] + s[:-i] == goal: return True
        
        return False
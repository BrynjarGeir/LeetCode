from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        op = {'(':')', '[':']', '{':'}'}; opened = deque();
        for c in s:
            if c in op.keys():
                opened.append(c)
            elif not opened: return False
            elif op[opened[-1]] == c:
                opened.pop()
            else: return False
        if opened: return False
        return True
                
                
            
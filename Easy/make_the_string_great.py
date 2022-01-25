class Solution:
    def makeGood(self, s: str) -> str:
        current = s; first = True
        while current != s or first:
            s = current; first = False; n = len(s) - 1
            for i in range(len(s)-1):
                if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
                    if i == n -1:
                        current = current[:i]
                    else:
                        current = current[:i] + current[i+2:]
                    break
        return current
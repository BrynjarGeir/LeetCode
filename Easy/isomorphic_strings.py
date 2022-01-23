class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        mapping = {}
        for i,v in enumerate(s):
            if v in mapping:
                if mapping[v] == t[i]: continue
                else: return False
            elif t[i] in mapping.values(): return False                
            else:
                mapping[v] = t[i]
        return True
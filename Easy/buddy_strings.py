from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        if s == goal and Counter(s).most_common(1)[0][1] > 1: return True
        elif s == goal: return False
        s = list(s); goal = list(goal)
        ind1 = None; ind2 = None
        for i in range(len(s)):
            if s[i] != goal[i] :
                if ind1 is None:
                    ind1 = i
                elif ind2 is None:
                    ind2 = i
                else: return False
        if ind1 is None or ind2 is None: return False
        tmp = s[ind1]; s[ind1] = s[ind2]; s[ind2] = tmp
        return s == goal
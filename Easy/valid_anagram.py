from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return set(s) == set(t) and len(s) == len(t) and Counter(s) == Counter(t)
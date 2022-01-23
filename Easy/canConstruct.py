class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = list(magazine)
        for c in ransomNote:
            if c in mag:
                mag.pop(mag.index(c))
            else: return False
        return True
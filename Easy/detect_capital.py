from string import ascii_lowercase as lowercase, ascii_uppercase as uppercase
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if all(c in lowercase for c in word): return True
        elif all(c in uppercase for c in word): return True
        elif word[0] in uppercase and all(c in lowercase for c in word[1:]): return True
        else: return False
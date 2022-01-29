class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiou'
        s1, s2 = s[:len(s)//2], s[len(s)//2:]
        return len([a for a in s1 if a.lower() in vowels]) == len([b for b in s2 if b.lower() in vowels])
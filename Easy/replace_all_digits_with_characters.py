from string import ascii_lowercase
class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = self.shift(s, s[i-1], int(s[i]))
        return ''.join(s)
            
        
    def shift(self, s, c, d):
        index = ascii_lowercase.index(c) + d
        return ascii_lowercase[index]
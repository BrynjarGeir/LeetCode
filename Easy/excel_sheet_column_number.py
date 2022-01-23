from string import ascii_uppercase
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = columnTitle[::-1]
        total = 0
        for e, c in enumerate(s):
            total += (ord(c) - 64) * (26**e)
        return total
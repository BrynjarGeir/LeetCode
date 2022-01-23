class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1 = 0; n2 = 0; o = 0
        for c in num1[::-1]:
            n1 += int(c)*10**o
            o += 1
        o = 0
        for c in num2[::-1]:
            n2 += int(c)*10**o
            o += 1
        return str(n1+n2)
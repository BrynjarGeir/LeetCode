class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0; n2 = 0; mapping = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
        num1 = num1[::-1]; p = 0
        for i in num1:
            n1 += mapping[i]*10**p
            p += 1
        num2 = num2[::-1]; p = 0
        for i in num2:
            n2 += mapping[i]*10**p
            p += 1
        total = n1 * n2
        return str(total)
            
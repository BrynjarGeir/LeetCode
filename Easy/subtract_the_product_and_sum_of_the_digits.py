from functools import reduce
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n%10)
            n //= 10
        sumDigits = sum(digits)
        productDigits = reduce((lambda x,y: x*y), digits)
        return productDigits - sumDigits
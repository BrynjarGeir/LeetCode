# Try somethings out saw basically this for someonelse but then tried 4sum rather than 2sum
# Was really not good enough the other was better in terms of speed but same memory
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend, divisor) == (-2**31, -1): return 2**31-1
        elif divisor == 1: return dividend
        elif divisor == -1: return -dividend
        elif divisor == dividend: return 1
        elif divisor == -dividend: return -1
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else 0
        dividend = abs(dividend); divisor = abs(divisor); currentSum = divisor; quotient = 0
        while dividend >= currentSum:
            quotientFour = 1
            while currentSum + currentSum + currentSum + currentSum <= dividend:
                currentSum += currentSum + currentSum + currentSum
                quotientFour += quotientFour + quotientFour + quotientFour
            dividend -= currentSum
            currentSum = divisor
            quotient += quotientFour
        return min(2**31-1, max(quotient if sign else -quotient, -2**31))
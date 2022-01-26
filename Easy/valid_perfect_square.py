from collections import Counter
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        def primeFactors(n):
            i = 2; factors = []
            while i * i <= n:
                if n%i: i+= 1
                else:
                    n //= i
                    factors.append(i)
            if n > 1: factors.append(n)
            return factors
        factors = primeFactors(num)
        if len(factors) % 2 != 0: return False
        counter = Counter(factors)
        if all(count % 2 == 0 for count in counter.values()): return True
        return False
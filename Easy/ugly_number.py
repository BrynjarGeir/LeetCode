class Solution:
    def isUgly(self, n: int) -> bool:
        def primeFactors(n):
            i = 2; factors = set()
            while i * i <= n:
                if n%i: i+= 1
                else:
                    n //= i
                    factors.add(i)
            if n > 1: factors.add(n)
            return factors
        if n < 1: return False
        if primeFactors(n).difference(set((2,3,5))) == set(): return True
        return False
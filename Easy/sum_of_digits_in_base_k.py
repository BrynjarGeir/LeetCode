class Solution:
    def sumBase(self, n: int, k: int) -> int:
        def numberToBase(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n%b))
                n //= b
            return digits[::-1]
        if k != 10:
            n = numberToBase(n,k)
            return sum(n)
        else:
            ans = 0
            print(n)
            while n > 0:
                print(n%10)
                ans += n%10
                n //= 10
            return ans
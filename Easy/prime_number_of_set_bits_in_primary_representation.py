class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = 0
        for i in range(left, right+1):
            curr = bin(i).count('1')
            if curr == 1: continue
            elif curr == 2 or curr == 3: primes += 1
            else:
                isPrime = True
                for j in range(2,curr//2+1):
                    if curr % j == 0:
                        isPrime = False
                        break
                if isPrime: primes += 1
                        
        return primes
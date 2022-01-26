from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        perms = list(permutations(range(1,n+1)))
        ans = [str(i) for i in perms[k-1]]
        return ''.join(ans)
from math import factorial
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1,n+1))
        ans = ''; k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, factorial(n))
            ans += str(numbers[index])
            numbers.remove(numbers[index])
        return ans
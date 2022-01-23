# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l +(r-l)//2
            curr = guess(mid)
            if curr == 0: return mid
            elif curr > 0: l = mid + 1
            else: r = mid
        return l
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, 2**31-1
        while l < r:
            mid = (l+r) // 2
            if mid * mid == x or (mid * mid < x and (mid + 1) * (mid + 1) > x): return mid
            elif mid * mid > x: r = mid
            else: l = mid + 1
        return l
            
            
        
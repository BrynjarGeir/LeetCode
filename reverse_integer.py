#This got accepted but I think I shouldn't have been allowed to use that y and then just check
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0: y = -int(str(x)[1:][::-1])
        else: y = int(str(x)[::-1])
        if y < -2**31 or y >= 2**31: return 0
        else: return y
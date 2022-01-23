class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        sign = 0 if num >= 0 else 1
        num = abs(num); ans = []
        while num > 0:
            ans.append(str(num % 7))
            num //= 7
        ans = ''.join(ans[::-1])
        if sign:
            return '-' + ans
        return ans
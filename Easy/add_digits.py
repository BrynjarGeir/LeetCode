class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10: return num
        while num >= 10:
            tmp = 0; curr = num
            while curr >= 1:
                tmp += curr % 10
                curr //= 10
            num = tmp
        return num
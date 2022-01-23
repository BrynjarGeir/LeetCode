from collections import deque
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else: keep = 1; pos = len(digits) - 1
        while keep:
            if pos == 0:
                if digits[pos] == 9:
                    digits = [1,0] + digits[1:]
                else: digits[pos] += 1
                return digits
            elif digits[pos] + 1 < 10:
                digits[pos] += 1
                return digits
            else:
                digits[pos] = 0
                pos -= 1
        return digits
                
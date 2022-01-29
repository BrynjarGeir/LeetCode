class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [int(c) for c in s if c.isdigit()]
        if not digits: return -1
        digits.sort(reverse = True)
        secondLargest = digits[0]
        for v in digits:
            if v != secondLargest:
                return v
        return -1class Solution:
    def secondHighest(self, s: str) -> int:
        digits = [int(c) for c in s if c.isdigit()]
        if not digits: return -1
        digits.sort(reverse = True)
        secondLargest = digits[0]
        for v in digits:
            if v != secondLargest:
                return v
        return -1
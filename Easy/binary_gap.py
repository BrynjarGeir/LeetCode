class Solution:
    def binaryGap(self, n: int) -> int:
        rep = bin(n)[2:]; longest = 0
        start, end, n = 0, 1, len(rep)
        while end < n:
            if rep[start] == '1' and rep[end] == '1':
                longest = end - start if end - start > longest else longest
                start = end; end += 1
            else:
                end += 1
        return longest
                
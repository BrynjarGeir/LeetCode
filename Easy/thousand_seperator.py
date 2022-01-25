class Solution:
    def thousandSeparator(self, n: int) -> str:
        m, dots = n, 0
        while m:
            m //= 1000
            if m: dots += 1
        n = str(n); i = len(n)-3
        while dots:
            n = n[:i] + '.' + n[i:]
            dots -= 1; i -= 3
        return n
            
from functools import reduce
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ans = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(ans, s, '') == reduce(ans, t, '')
from typing import List, inf
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h < len(piles): return inf
        elif h == len(piles): return max(piles)
        l, r = 1, max(piles)
        while l < r:
            mid = l + (r-l)//2
            if sum(ceil(p/mid) for p in piles) > h:
                l = mid + 1
            else:
                r = mid
        return l
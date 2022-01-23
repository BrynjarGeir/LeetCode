import numpy as np
from math import isclose
class Solution:
    def arrangeCoins(self, n: int) -> int:
        r = np.roots([1, 1, -2*n])
        if r[0] < 0 and isclose(int(r[1])+1, r[1], rel_tol = 1e-15): return int(r[1]) + 1
        elif r[0] < 0: return int(r[1])
        elif r[1] < 0 and isclose(int(r[0]) + 1,r[0], rel_tol = 1e-15): return int(r[0]) + 1
        else: return int(r[0])
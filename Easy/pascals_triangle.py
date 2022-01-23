from typing import List
from math import comb

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for i in range(numRows):
            curr = [1]
            for j in range(i):
                curr.append(comb(i, j+1))
            pascal.append(curr)
        return pascal   
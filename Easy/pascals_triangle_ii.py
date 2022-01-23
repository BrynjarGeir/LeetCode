from typing import List
from math import comb
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = []
        for i in range(rowIndex+1): 
            pascal.append(comb(rowIndex, i))
        return pascal
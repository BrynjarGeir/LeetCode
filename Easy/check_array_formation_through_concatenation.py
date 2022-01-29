import numpy as np
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        mp = {x[0]: x for x in pieces}
        ans = []
        
        for num in arr:
            ans += mp.get(num, [])
        
        return ans == arr
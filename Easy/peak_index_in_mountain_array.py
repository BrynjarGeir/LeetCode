import numpy as np
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return np.argsort(arr)[-1]

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))
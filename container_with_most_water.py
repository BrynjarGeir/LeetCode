import numpy as np

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxA = 0; i = 0; j = len(height) - 1
        while(i < j):
            area = (j-i)*min(height[i], height[j])
            if maxA < area: maxA = area
            if height[i] < height[j]: i += 1
            else: j -= 1
        return maxA
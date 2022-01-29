class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0; n = len(heights)
        left, right = [1]*n, [1]*n
        
        for i in range(n):
            j = i - 1
            while j >= 0:
                if heights[j] >= heights[i]:
                    left[i] += left[j]
                    j -= left[j]
                else: break
        
        for i in range(n-1, -1, -1):
            j = i + 1
            while j < n:
                if heights[j] >= heights[i]:
                    right[i] += right[j]
                    j += right[j]
                else: break
                    
        for i, h in enumerate(heights):
            maxArea = max(maxArea, h * (left[i] + right[i] - 1))
            
        return maxArea
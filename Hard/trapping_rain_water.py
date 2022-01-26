class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3: return 0
        trapped = 0
        # Maybe I should look at stuff like clipping of the ends
        # Like while it is ascending to the middle just ignore that part
        i = 0
        while i < len(height)-1:
            if height[i] < height[i+1]:
                i += 1
            else: break
        height = height[i:]
        i = len(height) - 1
        while i > 0:
            if height[i] < height[i-1]:
                i -= 1
            else: break
        height = height[:i+1]
        if len(height) < 3: return 0
        print(height)
        i = 1; curr = min(height[0], max(height[1:]))
        while i < len(height)-1:
            if curr > height[i]:
                trapped += curr - height[i]
            else:
                curr = min(height[i], max(height[i+1:]))
            i += 1
            
        return trapped
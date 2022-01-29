class Solution:
    def jump(self, nums: List[int]) -> int:
        n, start, end, ans, amax = len(nums)-1, 0, 0, 0, 0
        
        while True:
            for i in range(end, start-1, -1):
                if i >= n:
                    return ans
                
                amax = max(amax, i+nums[i])
            start = end + 1
            end = amax
            ans += 1
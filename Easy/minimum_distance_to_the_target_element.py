class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        if all(c == target for c in nums): return 0
        distR = inf
        for i in range(start, len(nums)):
            if nums[i] == target and i != start:
                distR = i - start
                break
        distL = inf
        for i in range(start, -1, -1):
            if nums[i] == target and i != start:
                distL = start - i
                break
        if distR == inf and distL == inf: return 0
        return min(distR, distL)
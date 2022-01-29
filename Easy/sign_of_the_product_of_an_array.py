class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums: return 0
        return 1 if len(list(filter(lambda x: x < 0, nums))) % 2 == 0 else -1
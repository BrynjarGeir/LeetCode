class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if 1 not in nums: return True
        start, end = nums.index(1), nums.index(1)+1
        while end < len(nums):
            if nums[start] == 1 and nums[end] == 1 and end - start <= k:
                return False
            elif nums[start] == 1 and nums[end] == 1:
                start = end
                end += 1
            else:
                end += 1
        return True
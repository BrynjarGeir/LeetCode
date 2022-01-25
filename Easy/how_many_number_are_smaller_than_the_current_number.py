class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        index = sorted(nums); n = len(index); ans = []
        for i in range(n):
            ans.append(index.index(nums[i]))
        return ans
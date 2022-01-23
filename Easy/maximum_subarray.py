from typing import List, inf
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = maxSum = -inf
        for i in nums:
            currSum = max(i, currSum + i)
            maxSum = max(maxSum, currSum)
        return maxSum 
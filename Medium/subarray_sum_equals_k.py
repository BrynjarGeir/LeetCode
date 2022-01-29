# Thanks to vijayzuzu
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0; sums = 0; mapping = {0:1}; n = len(nums)
        
        for i in range(n):
            sums += nums[i]
            count += mapping.get(sums - k, 0)
            mapping[sums] = mapping.get(sums, 0) + 1
        
        return count
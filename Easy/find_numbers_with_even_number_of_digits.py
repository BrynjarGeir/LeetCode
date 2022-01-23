from math import log10, floor
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            num_digits = floor(log10(num))+1
            if num_digits % 2 == 0:
                ans += 1            
        return ans
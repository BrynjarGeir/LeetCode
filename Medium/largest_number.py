from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        def cmp(a, b):
            return (a > b) - (a < b)
        
        nums = [str(num) for num in nums]
        
        nums.sort(key = cmp_to_key(lambda x,y: cmp(x+y, y+x)), reverse = True)                                
        
        return ''.join(nums).lstrip('0') or '0'
class Solution:
    def maximum69Number (self, num: int) -> int:
        nums = str(num)
        if '6' not in nums: return num
        for i,n in enumerate(nums):
            if n == '6' and i != len(nums)-1:
                nums = nums[:i] + '9' + nums[i+1:]
                break
            elif n == '6':
                nums = nums[:i] + '9'
                break
        return int(nums)
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x%2 == 0]
        odd = [y for y in nums if y%2 != 0]
        return even + odd
        
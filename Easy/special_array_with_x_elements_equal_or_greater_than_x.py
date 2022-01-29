class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = len(nums); nums.sort()
        for i in range(len(nums)):
            if all(c >= x for c in nums[i:]) and len(nums[i:]) == x and all(x > c for c in nums[:i]):
                return x
            x -= 1
        return -1
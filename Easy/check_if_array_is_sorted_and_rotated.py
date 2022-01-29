class Solution:
    def check(self, nums: List[int]) -> bool:
        # Let's just do the simple method of getting the first min index and then checking
        compare = sorted(nums)
        for i in range(len(nums)):
            compareL = compare[i:] + compare[:i]
            compareR = compare[-i:] + compare[:-1]
            if compareR == nums or compareL == nums:
                return True
        return False
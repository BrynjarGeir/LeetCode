class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums); target = []
        for i in range(n):
            if index[i] == len(target):
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target
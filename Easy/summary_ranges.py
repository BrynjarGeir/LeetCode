from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        currentRange = []; ans = []; i = 0; length = len(nums)
        while i < length:
            if len(currentRange) > 0:
                if currentRange[-1] == nums[i] - 1:
                    currentRange.append(nums[i]); i+= 1
                else:
                    if len(currentRange) > 1:
                        ans.append(str(currentRange[0]) + '->' + str(currentRange[-1]))
                        currentRange = []
                    else:
                        ans.append(str(currentRange[0]))
                        currentRange = []
            else:
                if i == length - 1:
                    ans.append(str(nums[i]))
                    return ans
                currentRange.append(nums[i]); i += 1
        if len(currentRange) > 1:
            ans.append(str(currentRange[0]) + '->' + str(currentRange[-1]))
        return ans
from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        x = sorted(x.items(), key = lambda item: (item[1], -item[0]))
        ans = []
        for item in x:
            for c in range(item[1]):
                ans.append(item[0])
        return ans
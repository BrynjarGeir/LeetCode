from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1 = Counter(nums1); count2 = Counter(nums2)
        n1 = set(nums1); n2 = set(nums2); inter = n1.intersection(n2)
        ans = []
        for i in inter:
            curr = min(count1[i], count2[i])
            for _ in range(curr):
                ans.append(i)
        return ans
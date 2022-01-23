from math import ceil, floor

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        complete = sorted(nums1+nums2)
        if len(complete) % 2 != 0:
            return complete[floor(len(complete) / 2)]
        else:
            upper = complete[int(len(complete)/2)]
            lower = complete[int(len(complete)/2 - 1)]
            return (upper + lower) / 2
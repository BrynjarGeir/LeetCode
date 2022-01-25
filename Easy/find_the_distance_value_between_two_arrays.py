class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        distance = 0
        for element in arr1:
            if not any(c for c in arr2 if abs(c-element) <= d):
                distance += 1
        return distance
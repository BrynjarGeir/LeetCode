class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for i,v in enumerate(nums):
            if v in mapping and i - mapping[v] <= k: return True
            mapping[v] = i
        return False
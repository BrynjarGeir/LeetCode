class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1,-1]
        return self.search(nums, 0, len(nums)-1, target)
    
    def search(self, nums, start, end, target):
        if nums[start] == nums[end] == target:
            return [start, end]
        elif nums[start] <= target <= nums[end]:
            mid = start + (end - start)//2
            l, r = self.search(nums, start, mid, target), self.search(nums, mid+1, end, target)
            return max(l,r)  if -1 in l+r else [l[0],r[1]]
        return [-1,-1]
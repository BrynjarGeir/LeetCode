class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        for i in nums1:
            ind = nums2.index(i); added = False
            for j in range(ind+1,len(nums2)):
                if nums2[j] > i: 
                    ans.append(nums2[j]); added = True
                    break
            if not added: ans.append(-1)
        return ans
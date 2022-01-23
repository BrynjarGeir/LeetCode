class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for item in arr2:
            curr = [i for i,x in enumerate(arr1)  if x == item]
            for tick in curr:
                ans.append(arr1[tick])
        s = [x for x in arr1 if x not in arr2]
        s.sort()
        ans = ans + s
        return ans
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr); ans = [0]*n
        for i in range(n):
            if i == n-1: ans[i] = -1
            else:
                ans[i] = max(arr[i+1:])
        return ans
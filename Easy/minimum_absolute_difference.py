class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        minimumDiff = 2**31-1; pairs = []
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < minimumDiff:
                minimumDiff = arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] == minimumDiff:
                pairs.append([arr[i],arr[i+1]])
        return pairs
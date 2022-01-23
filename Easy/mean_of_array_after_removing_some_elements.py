class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)//20
        arr = arr[n:len(arr)-n] 
        return sum(arr) / len(arr)
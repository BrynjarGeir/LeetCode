class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: return False
        top = max(arr)
        if arr.count(top) != 1: return False
        ind = arr.index(top)
        if ind == 0 or ind == len(arr)-1: return False
        pre = arr[:ind]; post = arr[ind+1:]
        b1 = False; b2 = False
        if len(arr) == 3: return True
        for i in range(1,len(pre)):
                if pre[i] <= pre[i-1]:
                    return False
        for i in range(len(post)-1):
                if post[i] <= post [i+1]:
                    return False
        return True
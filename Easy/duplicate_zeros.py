class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = j = 0; n = len(arr)
        c = arr[:]
        while j < n:
            arr[j] = c[i]
            j += 1
            if c[i] == 0:
                if j < n: arr[j] = c[i]
                j += 1
            i += 1
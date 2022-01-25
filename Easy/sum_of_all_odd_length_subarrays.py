class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return arr[0]
        elif n == 2: return arr[0] + arr[1]
        else:
            total = 0
            for odd in range(1,n+1):
                if odd % 2 == 0: continue
                start = 0
                while start + odd <= n:
                    total += sum(arr[start:start+odd])
                    start += 1
        return total
class Solution:
    def countLargestGroup(self, n: int) -> int:
        dp = {0:0}; count = [0]*(4*9)
        for i in range(1,n+1):
            q, r = divmod(i,10)
            dp[i] = r + dp[q]
            count[dp[i]-1] += 1
        return count.count(max(count))
            
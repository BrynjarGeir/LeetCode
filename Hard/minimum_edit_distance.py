class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
                
        return self.med(word1, word2, len(word1), len(word2))
    
    def med(self, word1, word2, n, m):
        
        dp = [[0 for _ in range(m+1) ] for _ in range(n+1)]
        ptr = [['' for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
        for j in range(m+1):
            dp[0][j] = j
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                sub = dp[i-1][j-1] + 1 if word1[i-1] != word2[j-1] else dp[i-1][j-1]
                ins = dp[i][j-1] + 1
                dele = dp[i-1][j] + 1
                dp[i][j] = min(sub, ins, dele)
                        
        return dp[n][m]
                
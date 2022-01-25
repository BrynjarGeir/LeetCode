class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1,len(s)):
            currScore = s[:i].count('0') + s[i:].count('1')
            score = max(score, currScore)
        return score
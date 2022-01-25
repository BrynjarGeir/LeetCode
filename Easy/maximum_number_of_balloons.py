from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        countBalloon = Counter('balloon')
        return min(counter[c]//countBalloon[c] for c in countBalloon)
            
            
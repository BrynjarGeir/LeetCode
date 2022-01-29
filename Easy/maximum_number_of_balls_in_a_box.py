class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        counts = {}
        for d in range(lowLimit, highLimit+1):
            curr = sum(map(int, str(d)))
            if curr not in counts:
                counts[curr] = 1
            else:
                counts[curr] += 1
        return max(counts.items(), key = lambda x: x[1])[1]
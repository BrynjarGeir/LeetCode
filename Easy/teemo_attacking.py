class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisonedTime = 0
        while len(timeSeries) > 1:
            if duration < timeSeries[1] - timeSeries[0]:
                poisonedTime += duration
            else:
                poisonedTime += timeSeries[1] - timeSeries[0]
            timeSeries.pop(0)
        poisonedTime += duration
        return poisonedTime
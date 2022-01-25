class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        keys = list(keysPressed); values = []
        for ind in range(len(releaseTimes)):
            if ind == 0: 
                values.append(releaseTimes[ind])
            else:
                values.append(releaseTimes[ind] - releaseTimes[ind-1])
        mapping = max(zip(values, keys))
        return mapping[1]
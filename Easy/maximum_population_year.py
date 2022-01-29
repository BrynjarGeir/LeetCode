class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        birthrate = {}
        for log in logs:
            for alive in range(log[0],log[1]):
                if alive in birthrate:
                    birthrate[alive] += 1
                else:
                    birthrate[alive] = 1
        return max(birthrate.items(), key = lambda x: (x[1],-x[0]))[0]
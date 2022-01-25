class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        keys = [c for c in range(1,n+1)]; values = [0]*n
        counting = dict(zip(keys, values))
        counting[rounds[0]] += 1
        for i in range(len(rounds)-1):
            start, end = rounds[i], rounds[i+1]
            while start != end:
                if start == n:
                    start = 1
                else: start += 1
                counting[start] += 1
        maxValue = max(counting.values())
        ans = []
        for key in counting:
            if counting[key] == maxValue:
                ans.append(key)
        return ans
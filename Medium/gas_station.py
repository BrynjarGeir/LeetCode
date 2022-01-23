class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n, status, total, index = len(gas), 0, 0, 0
        for i in range(n):
            total += gas[i] - cost[i]
            status += gas[i] - cost[i]
            if status < 0:
                status = 0; index = i + 1
        return -1 if total < 0 else index
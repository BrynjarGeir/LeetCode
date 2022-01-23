from collections import deque
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = deque(sorted(stones))
        while len(stones) > 1:
            heavy, light = stones.pop(), stones.pop()
            if heavy == light: continue
            heavy -= light
            stones.append(heavy)
            stones = sorted(stones)
        if stones: return stones[0]
        return 0
        
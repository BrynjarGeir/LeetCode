class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1: return 1
        power = 1; maxPower = 1; prev = None
        for c in s:
            if prev == None or prev != c: 
                prev = c
                maxPower = max(maxPower, power)
                power = 1
                continue
            elif c == prev:
                power += 1
                maxPower = max(maxPower, power)
        return maxPower
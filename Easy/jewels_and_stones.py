class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j = 0
        for stone in stones:
            if stone in jewels:
                j += 1
        return j
# or better off of https://leetcode.com/problems/jewels-and-stones/discuss/113574/1-liners-PythonJavaRuby
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(map(jewels.count, stones))
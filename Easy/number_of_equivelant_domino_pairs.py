from collections import Counter
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        return int(sum(s*(s-1)/2 for s in Counter(tuple(sorted(x)) for x in dominoes).values()))
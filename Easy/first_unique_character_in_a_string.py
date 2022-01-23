from operator import itemgetter
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = Counter(s)
        if min(counter.items(), key=itemgetter(1))[1] >= 2: return -1
        for i,c in enumerate(s):
            if counter[c] == 1: return i
        
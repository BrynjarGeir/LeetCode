from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = s1.split(); s2 = s2.split(); ans = []
        s1 = Counter(s1); s2 = Counter(s2); total = set(s1+s2)
        for word in total:
            if word in s1 and s1[word] == 1 and word not in s2:
                ans.append(word)
            elif word in s2 and s2[word] == 1 and word not in s1:
                ans.append(word)
        return ans
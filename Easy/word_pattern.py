class Solution:
    def getUnique(self, seq: list) -> list:
        seen = set(); seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]
    
    def wordPattern(self, pattern: str, s: str) -> bool:
        p = [c for c in pattern]; words = s.split(' ')
        if len(p) != len(words): return False
        seen = set(); seen_add = seen.add
        pSeq = [x for x in p if not (x in seen or seen_add(x))]
        seen = set(); seen_add = seen.add
        wordsSeq = [x for x in words if not (x in seen or seen_add(x))]
        mapping = {}
        for i in range(len(pSeq)): 
            mapping[pSeq[i]] = wordsSeq[i]
        print(mapping)
        for i in range(len(words)): 
            print('Mapping',mapping[p[i]])
            print('Words',words[i])
            if mapping[p[i]] != words[i]: return False
        return True
        
    
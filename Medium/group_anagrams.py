class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            curr = ''.join(sorted(list(s)))
            if curr not in anagrams:
                anagrams[curr] = [s]
            else:
                anagrams[curr].append(s)
        
        return anagrams.values()
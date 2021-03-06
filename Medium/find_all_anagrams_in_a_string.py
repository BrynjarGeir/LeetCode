class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p): return
        letters = [0]*26
        ans = []
        for c in p:
            letters[ord(c) - 97] += 1
        
        j = 0
        remaining = len(p)
        
        for i in range(0, len(s)):
            while j < len(s) and j - i < len(p):
                freq = letters[ord(s[j]) - 97]
                if freq > 0: remaining -= 1
                letters[ord(s[j]) - 97] -= 1
                j += 1
            index = ord(s[i]) - 97
            
            if remaining == 0 and j - i == len(p):
                ans.append(i)
            
            if  letters[index] >= 0: remaining += 1
            letters[index] += 1
        return ans
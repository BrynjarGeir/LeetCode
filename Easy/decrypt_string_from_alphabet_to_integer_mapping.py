from string import ascii_lowercase
class Solution:
    def freqAlphabets(self, s: str) -> str:
        keys = [str(i) for i in range(1,10)] + [str(i)+'#' for i in range(10,27)]
        values = ascii_lowercase
        mapping = dict(zip(keys, values))
        ans = []
        if len(s) == 1: return mapping[s]
        if len(s) == 2: return mapping[s[0]] + mapping[s[1]]
        while s:
            if len(s) > 2 and s[:3] in mapping:
                ans.append(mapping[s[:3]])
                s = s[3:]
            else:
                ans.append(mapping[s[0]])
                s = s[1:]
        return ''.join(ans)
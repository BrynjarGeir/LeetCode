from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(min(strs, key=len))
        while l > 0:
            if all(prefix[:l] == strs[0][:l] for prefix in strs):
                return strs[0][:l]
            else: l -= 1
        return ''
        
from collections import deque
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        tip = s.replace('-',''); num = len(tip) // k; position = len(tip)
        ans = deque()
        while num > 0:
            ans.appendleft(tip[position-k:position])
            position -= k; num -= 1
        if position > 0: ans.appendleft(tip[0:position])
        return '-'.join(ans).upper()
            
                
        
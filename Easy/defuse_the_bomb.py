class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0: return [0]*len(code)
        ans = []; n = len(code)
        for i in range(n):
            if i == n-1 and k > 0:
                ans.append(sum(code[:k]))
            elif i + k >= len(code):
                ans.append(sum(code[i+1:]) + sum(code[:i+k-n+1]))
            elif i == 0 and k < 0:
                ans.append(sum(code[k:]))
            elif i + k <= -1:
                ans.append(sum(code[:i]) + sum(code[n+k+i:]))
            elif k > 0:
                ans.append(sum(code[i+1:i+k+1]))
            elif k < 0:
                ans.append(sum(code[i+k:i]))
        return ans
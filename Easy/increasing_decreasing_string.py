class Solution:
    def sortString(self, s: str) -> str:
            if len(s) == 1: return s
            seen = []; letters = sorted(list(set(s))); ans = ''; s = list(s); n = len(letters)
            while s:
                curr = ''; i = 0
                while i < len(letters):
                    if letters[i] in s:
                        curr = curr + letters[i]
                        s.remove(letters[i])
                        i += 1
                    else:
                        letters.remove(letters[i])
                ans = ans + curr
                curr = ''; i = len(letters)-1
                while i > -1:
                    if letters[i] in s:
                        curr = curr + letters[i]
                        s.remove(letters[i])
                        i -= 1
                    else:
                        letters.remove(letters[i])
                        i -= 1
                ans = ans + curr
            return ans
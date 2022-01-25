class Solution:
    def reformat(self, s: str) -> str:
        digits = [c for c in s if c.isdigit()]
        letters = [c for c in s if not c.isdigit()]
        n = len(digits); m= len(letters)
        if n > m+1 or m > n+1: return ''
        elif n > m:
            ans = ''
            while letters:
                ans = ans + digits.pop() + letters.pop()
            return ans + digits.pop()
        elif n < m:
            ans = ''
            while digits:
                ans = ans + letters.pop() + digits.pop()
            return ans + letters.pop()
        else:
            ans = ''
            while digits:
                ans = ans + digits.pop() + letters.pop()
            return ans
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x < 10: return True
        if x < 0 or x % 10 == 0: return False
        return x == int(str(x)[::-1])
        
        
class Solution:
    
    def isFloat(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    def myAtoi(self, s: str) -> int:        
        s = s.lstrip(' ').rstrip(' ')
        s = s.split(' ')[0]
        
        for i in range(len(s)):
            if not s[i].isnumeric() and i != 0:
                s = s[:i]; break
        
        first = not s.isnumeric() and not (s[1:].isnumeric() and (s[0]=='+' or s[0]=='-'))
        second = not self.isFloat(s) or not self.isFloat(s[1:])
        
        if first and second: return 0
        
        if s[0] == '+': pos = True; signed = True; s = s[1:]
        elif s[0] == '-': pos = False; signed = True; s = s[1:]
        else: signed = False
    
        if '.' in s: s = s[:s.index('.')]
        if s == '': return 0
        if signed and not pos: x = -int(s)
        else: x = int(s)
            
        if x < -2**31: x = -2**31
        elif x >= 2**31: x = 2**31-1
        
        return x
            
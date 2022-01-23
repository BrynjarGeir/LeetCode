class Solution:
    def findComplement(self, num: int) -> int:
        bits = bin(num)[2:]; compl = ''
        for bit in bits:
            if bit == '1': compl = compl + '0'
            else: compl = compl + '1'
        return int(compl, 2)
class Solution:
    def findComplement(self, num: int) -> int:
        mapping = {'1':'0', '0':'1'}
        bits = bin(num)[2:]
        ans = ''.join(mapping[x] for x in bits)
        return int(ans, 2)
        
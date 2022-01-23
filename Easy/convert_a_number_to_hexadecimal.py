class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return '0'
        ans = ''; sign = 1 if num < 0 else 0; num = abs(num)
        mapping = {0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        if sign:
            binaryRep = '{:032b}'.format(num)
            negBinaryRep = ''.join('1' if x == '0' else '0' for x in binaryRep)
            i = len(negBinaryRep) - 1
            while i >= 0:
                if negBinaryRep[i] == '0' and i != len(negBinaryRep)-1:
                    negBinaryRep = negBinaryRep[:i] + '1' + negBinaryRep[i+1:]
                    break
                elif negBinaryRep[i] == '0':
                    negBinaryRep = negBinaryRep[:i] + '1'
                    break
                elif negBinaryRep[i] == '1' and i != len(negBinaryRep)-1:
                    negBinaryRep = negBinaryRep[:i] + '0' + negBinaryRep[i+1:]
                else:
                    negBinaryRep = negBinaryRep[:i] + '0'
                i -= 1
            num = int(negBinaryRep, 2)
        while num > 0:
            rem = num%16
            ans = mapping[rem] + ans
            num //= 16        
        return ans
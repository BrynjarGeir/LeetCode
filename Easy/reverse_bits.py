class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(16):
            ans |= ((n>>i)&1)<<(31-i) | ((n>>(31-i))&1) << i
        return ans
    
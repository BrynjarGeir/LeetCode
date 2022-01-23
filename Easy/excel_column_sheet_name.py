from string import ascii_uppercase
from collections import deque
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = list(ascii_uppercase)
        ans = deque()
        while columnNumber > 0:
            ans.appendleft(capitals[(columnNumber-1)%26])
            columnNumber = (columnNumber - 1)//26
        return ''.join(ans)
        
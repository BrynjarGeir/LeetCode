from collections import deque

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        rows = list(range(numRows)); row = 0; s = deque([c for c in s])
        dictionary = dict.fromkeys(rows, ''); down = True
        maxRow = numRows-1
        while s:
            dictionary[row] += s.popleft()
            if down and row < maxRow:
                row += 1
            elif down and row == maxRow:
                down = False; row -= 1
            elif not down and row > 0:
                row -= 1
            elif not down and row == 0:
                down = True; row += 1
        a = deque([dictionary[x] for x in sorted(dictionary.keys())]); b = ''
        while a:
            b += a.popleft()
        return b
            
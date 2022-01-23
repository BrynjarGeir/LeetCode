class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        s = list(s); lines = 1; line = 0
        while s:
            if line + widths[ord(s[0])-97] > 100:
                lines += 1; line = 0
            else:
                line += widths[ord(s.pop(0))-97]
        return [lines, line]
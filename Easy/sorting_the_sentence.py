class Solution:
    def sortSentence(self, s: str) -> str:
        ans = []; s = s.split()
        s = sorted(s, key=lambda x: x[-1])
        s = [c[:len(c)-1] for c in s]
        return ' '.join(s)
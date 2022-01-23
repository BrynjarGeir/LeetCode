class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = []
        for word in words:
            ch = list(chars); b = True
            for c in word:
                if c not in ch:
                    b = False; break
                ch.pop(ch.index(c))
            if b: ans.append(word)
        return len(''.join(ans))
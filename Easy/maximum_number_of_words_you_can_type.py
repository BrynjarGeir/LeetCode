class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split(); blSet = set(brokenLetters); number = 0
        for word in text:
            if set(word) & blSet: continue
            else: number += 1
        return number
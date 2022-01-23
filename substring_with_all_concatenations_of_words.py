from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_size = len(words[0]); sublength = word_size * len(words)
        if sublength > len(s): return None
        word_map = Counter(words); indexes = set(); words_length = len(words)
        for i in range(len(s) - sublength + 1):
            seen = dict(word_map); word_used = 0
            for j in range(i, i + sublength, word_size):
                if s[j:j+word_size] in words and seen[s[j:j+word_size]] > 0:
                    seen[s[j:j+word_size]] -= 1
                    word_used += 1
                else: break
            if word_used == words_length: indexes.add(i)
        return indexes
        
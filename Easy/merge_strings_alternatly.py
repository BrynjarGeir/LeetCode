from collections import deque
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = deque(); word1 = deque(word1); word2 = deque(word2)
        
        while word1 and word2:
            word.append(word1.popleft())
            word.append(word2.popleft())
        if word1:
            word += word1
        else:
            word += word2
        return ''.join(word)
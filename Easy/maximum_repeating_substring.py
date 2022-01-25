class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k = 0
        while True:
            if k*word in sequence: k += 1
            else: break
        return k-1
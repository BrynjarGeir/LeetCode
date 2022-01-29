from string import ascii_lowercase
class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        sentence = ''
        for c in word:
            if c in ascii_lowercase:
                sentence = sentence + ' '
            else:
                sentence = sentence + c
        sentence = sentence.split()
        sentence = [int(c) for c in sentence]
        return len(set(sentence))
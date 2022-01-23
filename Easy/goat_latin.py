class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set(['a','A','e','E','i','I','o','O','u','U'])
        sentence = sentence.split(); ans = ''; p = 'a'
        for ind, word in enumerate(sentence):
            if word[0] in vowels:
                word = word + 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word = word + p
            sentence[ind] = word
            p = p + 'a'
        return ' '.join(sentence)
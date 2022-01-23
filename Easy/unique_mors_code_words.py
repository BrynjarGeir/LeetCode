from string import ascii_lowercase
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        values = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        keys = ascii_lowercase
        mapping = dict(zip(keys,values))
        w = set()
        for word in words:
            w.add((''.join([mapping[c] for c in word])))
        return len(w)
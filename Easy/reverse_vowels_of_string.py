class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}; n = len(s)
        ll = [x for x in s[::-1] if x in vowels]
        for i in range(n):
            if s[i] in vowels:
                s = s[:i] + ll.pop(0) + s[i+1:]
        return s
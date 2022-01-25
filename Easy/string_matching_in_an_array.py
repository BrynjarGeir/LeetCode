class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for word in words:
            if any(word in w for w in words if word != w):
                ans.append(word)
        return ans
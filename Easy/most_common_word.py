from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z ,]','',paragraph).lower().replace(',',' ').replace(';',' ').replace(':',' ').split()
        paragraph = [word for word in paragraph if word not in banned]
        count = Counter(paragraph)
        return max(count, key = count.get)
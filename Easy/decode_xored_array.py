class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]
        for enc in encoded:
            arr.append(enc^arr[-1])
        return arr
        
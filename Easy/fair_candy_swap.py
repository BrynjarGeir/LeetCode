class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        dif = (sum(aliceSizes) - sum(bobSizes))/2
        a = set(aliceSizes)
        for b in set(bobSizes):
            if dif + b in a:
                return [dif + b, b]

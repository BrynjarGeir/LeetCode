class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arb = [(bin(n)[2:].count('1'), n) for n in arr]
        arb = sorted(arb, key = lambda element: (element[0], element[1]))
        arb = [x[1] for x in arb]
        return arb
        
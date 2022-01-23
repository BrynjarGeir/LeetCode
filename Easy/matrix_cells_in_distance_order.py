class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        mapping = {}; ans = []
        for i in range(rows):
            for j in range(cols):
                dist = abs(i-rCenter) + abs(j-cCenter)
                if dist in mapping:
                    mapping[dist].append((i,j))
                else:
                    mapping[dist] = [(i,j)]
        for key in sorted(mapping.keys()):
            ans += mapping[key]
        return ans
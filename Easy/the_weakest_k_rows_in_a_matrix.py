class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []; i = 0
        for row in mat:
            ans.append((i, row.count(1))); i+= 1
        
        ans = sorted(ans, key = lambda element: (element[1], element[0]))
        
        ans = [x[0] for x in ans]
        
        return ans[:k]
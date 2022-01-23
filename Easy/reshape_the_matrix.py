class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if len(mat)*len(mat[0]) != r*c: return mat
        mat = [item for row in mat for item in row]; ans = []
        for i in range(r):
            tmp = []
            for j in range(c):
                tmp.append(mat.pop(0))
            ans.append(tmp)
        return ans
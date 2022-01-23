class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        rows = [0]*3; cols = [0]*3; diag1 = 0; diag2 = 0
        for ind, move in enumerate(moves):
            i, j = move
            sign = 1 if ind % 2 == 0 else -1
            rows[i] += sign
            cols[j] += sign
            if i == j: diag1 += sign
            if i + j == 2: diag2 += sign
            if abs(rows[i]) == 3 or abs(cols[j]) == 3 or abs(diag1) == 3 or abs(diag2) == 3:
                return 'A' if sign == 1 else 'B'
        return 'Draw' if len(moves) == 9 else 'Pending'
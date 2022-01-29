from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board); m = len(board[0]); nxtLetter = deque(word)
        path = (0,0)
    
        def dfs(board, i, j, word):
            if len(word) == 0:
                return True
            if i < 0 or i >= n or j < 0 or j >= m or word[0] != board[i][j]:
                return False
            
            tmp = board[i][j]
            board[i][j] = '#'
        
        
            ans = (dfs(board, i + 1, j, word[1:]) or dfs(board, i - 1, j, word[1:])
                    or dfs(board, i, j + 1, word[1:]) or dfs(board, i, j - 1, word[1:]))
            
            board[i][j] = tmp
                        
            return ans
            
        
        for i in range(n):
            for j in range(m):
                if dfs(board, i, j, word):
                    print('Ég kemst hingað þegar að ég á ekki að komast hingað!')
                    print('Þá er board',board)
                    print('Og i,j',i,j)
                    print('Og loks auðvitað word',word)
                    return True
        return False        
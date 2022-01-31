from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []; trie = Trie(); node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, '', ans)
        return ans
        
    
    def dfs(self, board, node, i, j, p, ans):
        if node.is_word:
            ans.append(p)
            node.is_word = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i - 1, j, p + tmp, ans)
        self.dfs(board, node, i + 1, j, p + tmp, ans)
        self.dfs(board, node, i, j - 1, p + tmp, ans)
        self.dfs(board, node, i, j + 1, p + tmp, ans)
        board[i][j] = tmp
        

class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False
        
class Trie():
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.is_word = True
        
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word
        
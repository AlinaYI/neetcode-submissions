class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        def backtrack(i, j, node, comb):
            seen[i][j] = True
            if node.end == True:
                res.append(comb)
                node.end = False
            
            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and seen[ni][nj] == False:
                    nextChar = board[ni][nj]
                    if nextChar in node.children:
                        backtrack(ni, nj, node.children[nextChar], comb + nextChar)

            seen[i][j] = False

        res = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = [[False]*len(board[0]) for _ in range(len(board))]
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if board[i][j] in root.children:
                    backtrack(i, j, root.children[board[i][j]], board[i][j])
        return res
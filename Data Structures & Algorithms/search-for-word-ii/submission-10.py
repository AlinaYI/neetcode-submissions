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
        
        def backtrack(i,j, node, comb):
            if node.end == True:
                res.append(comb)
                node.end = False

            seen.add((i,j))
            for di, dj in directions:
                ni, nj = di+i, dj+j
                if 0<=ni<row and 0<=nj<col and board[ni][nj] in node.children and (ni,nj) not in seen:
                    newNode = board[ni][nj]
                    backtrack(ni,nj,node.children[newNode], comb+newNode)
            seen.remove((i,j))

        res = []
        row, col = len(board), len(board[0])
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(row):
            for j in range(col):
                if board[i][j] in root.children:
                    char = board[i][j]
                    backtrack(i,j,root.children[char], char)
        return res
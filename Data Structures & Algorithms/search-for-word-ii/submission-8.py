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
        
        # buildTree
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        # backtrack()
        def backtrack(i, j, node, comb):
            seen.add((i,j))
            if node.end == True:
                res.append(comb)
                node.end = False

            for di, dj in directions:
                ni, nj = i+di, j+dj
                if 0<=ni<row and 0<=nj<col and (ni,nj) not in seen:
                    nextChar = board[ni][nj]
                    if nextChar in node.children:
                        backtrack(ni, nj, node.children[nextChar], comb+nextChar)
            seen.remove((i,j))
        
        row, col = len(board), len(board[0])
        seen = set()
        res = []
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(row):
            for j in range(col):
                if board[i][j] not in root.children:
                    continue
                backtrack(i, j, root.children[board[i][j]], board[i][j])
        return res

        
                
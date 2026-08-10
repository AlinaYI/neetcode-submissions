class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, words):
        curr = self
        for c in words:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # build TrieTree
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        
        def backtrack(i, j, node, comb):

            seen[i][j] = True
            currChar = board[i][j]
            comb += currChar

            currNode = node.children[currChar]
            if currNode.end == True:
                res.append(comb)
                # avoid duplicate result
                currNode.end = False
            
            for di, dj in directions:
                ni,nj = i+di, j+dj
                if 0<=ni<len(board) and 0<=nj<len(board[0]) and seen[ni][nj] == False and board[ni][nj] in currNode.children:
                    backtrack(ni, nj, currNode, comb)

            seen[i][j] = False

        res = []
        seen = [[False]*len(board[0]) for _ in range(len(board))]
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    backtrack(i,j, root, "")
        return res

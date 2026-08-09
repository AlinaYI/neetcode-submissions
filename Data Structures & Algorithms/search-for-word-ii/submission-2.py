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
        
        res = []
        seen = [[False]*len(board[0]) for _ in range(len(board))]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def backtrack(i,j, node, comb):
            if not(0<=i<len(board)) or not (0<=j<len(board[0])) or seen[i][j] == True or board[i][j] not in node.children:
                return
            
            seen[i][j] = True
            currChar = board[i][j]
            comb += currChar

            currNode = node.children[currChar]
            if currNode.end == True:
                res.append(comb)
                currNode.end = False
            
            for di,dj in directions:
                ni, nj = i+di, j+dj
                backtrack(ni,nj,currNode, comb)
            
            seen[i][j] = False
            
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i,j,root, "")
        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def AddWord(self, word):
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
            root.AddWord(word)

        res = []
        seen = set()
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def backtrack(i, j, node, comb):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or (i,j) in seen or board[i][j] not in node.children:
                return
            
            seen.add((i,j))
            char = board[i][j]
            curr_node = node.children[char]
            comb += char
            if curr_node.end == True:
                res.append(comb)
                curr_node.end = False
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                backtrack(ni, nj, curr_node, comb)
            
            seen.remove((i,j))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i,j,root,"")
        return res
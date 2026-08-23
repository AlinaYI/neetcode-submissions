class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]= TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(idx, node):
            if idx == len(word):
                return node.end

            currChar = word[idx]
            if currChar == ".":
                for letter in node.children.values():
                    if dfs(idx+1, letter):
                        return True
                return False
            if currChar not in node.children:
                return False
            return dfs(idx+1, node.children[currChar]) 
        
        return dfs(0, self.root)

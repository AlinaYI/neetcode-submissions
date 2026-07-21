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
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, idx):
            if idx == len(word):
                return node.end
            
            if word[idx] == ".":
                for letter in node.children.values():
                    if dfs(letter, idx + 1):
                        return True
            
            if word[idx] not in node.children:
                return False
            
            return dfs(node.children[word[idx]], idx + 1)


        return dfs(self.root, 0)
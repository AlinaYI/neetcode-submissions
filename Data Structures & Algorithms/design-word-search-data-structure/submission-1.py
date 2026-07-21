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
        
        def dfs(node, start):
            if start == len(word):
                return node.end
            
            # searching char
            char = word[start]
            if char == ".":
                # day
                for letter in node.children.values():
                    if dfs(letter, start + 1):
                        return True
                return False
            
            # we do not have this in node
            if char not in node.children:
                return False
            
            return dfs(node.children[char], start + 1)
            # dfs("d", 1)

        return dfs(self.root, 0)

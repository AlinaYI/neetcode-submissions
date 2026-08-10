class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        front = {beginWord}
        back = {endWord}

        if endWord not in wordSet:
            return 0
        step = 1
        while front and back:

            if len(front) > len(back):
                front, back = back, front
            
            nextFront = set()
            for word in front:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in back:
                            return step + 1
                        
                        if newWord in wordSet:
                            nextFront.add(newWord)
                            wordSet.remove(newWord)
            front = nextFront
            step += 1
        return 0
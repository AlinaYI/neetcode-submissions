class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        front = {beginWord}
        back = {endWord}
        step = 1

        while front and back:

            if len(front) > len(back):
                front, back = back,front

            next_front = set()
            for word in front:
                for idx in range(len(word)):
                    for c in "abcdefghijklnmopqrstuvwxyz":
                        newWord = word[:idx] + c + word[idx+1:]
                        if newWord in back:
                            return step + 1
                            
                        if newWord in wordSet:
                            next_front.add(newWord)
                            wordSet.remove(newWord)
            front = next_front
            step += 1
        return 0
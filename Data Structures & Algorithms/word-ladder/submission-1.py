class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordSet = set(wordList)

        q = deque([(beginWord, 1)])
        while q:
            word, step = q.popleft()
            if word == endWord:
                return step

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]

                    if newWord in wordSet:
                        q.append((newWord, step + 1))
                        wordSet.remove(newWord)
        return 0
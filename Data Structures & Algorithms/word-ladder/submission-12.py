class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        while q:
            curr, step = q.popleft()
            if curr == endWord:
                return step
            
            for i in range(len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = curr[:i] + c + curr[i+1:]
                    if newWord in wordSet:
                        q.append((newWord, step+1))
                        wordSet.remove(newWord)
        return 0
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endWord not in wordList:
        #     return 0
        
        # wordSet = set(wordList)

        # q = deque([(beginWord, 1)])
        # while q:
        #     word, step = q.popleft()
        #     if word == endWord:
        #         return step

        #     for i in range(len(word)):
        #         for c in "abcdefghijklmnopqrstuvwxyz":
        #             newWord = word[:i] + c + word[i+1:]

        #             if newWord in wordSet:
        #                 q.append((newWord, step + 1))
        #                 wordSet.remove(newWord)
        # return 0

    
##
        # Time:  O(N × L²)
        # Space: O(N × L)
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        front, back = {beginWord}, {endWord}
        step = 1

        while front and back:
            if len(front) > len(back):
                front, back = back, front
            
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in back:
                            return step + 1
                        
                        if newWord in wordSet:
                            next_front.add(newWord)
                            wordSet.remove(newWord)
            front = next_front
            step += 1
        return 0
    
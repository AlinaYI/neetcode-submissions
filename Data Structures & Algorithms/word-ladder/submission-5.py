class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        这里的思路就是一个个换，一个个search
        每次改一个字母，然后看newWord是不是再wordList里
        '''
        # dfs / bfs
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        front = {beginWord}
        back = {endWord}
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
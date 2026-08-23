class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        方法	Worst-caseTC    SC	        实际搜索空间
        BFS	    O(N * L²)	    O(N)	    约 O(b^d)
        双向BFS	O(N * L²)  worst caseO(N)	约 O(b^(d/2))
        '''
        wordSet = set(wordList)
        begin = {beginWord}
        end = {endWord}

        if endWord not in wordSet:
            return 0
        step = 1

        while begin and end:
            if len(begin) > len(end):
                begin, end = end, begin
            
            nextLevel = set()
            for word in begin:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in end:
                            return step + 1
                        if newWord in wordSet:
                            nextLevel.add(newWord)
                            wordSet.remove(newWord)
            begin = nextLevel
            step += 1
        return 0


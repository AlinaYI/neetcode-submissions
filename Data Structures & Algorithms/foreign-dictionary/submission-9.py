class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        wordDict = {c:set() for word in words for c in word}
        indegree = {c:0 for c in wordDict}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""
            
            for idx in range(minLen):
                if word2[idx] != word1[idx]:
                    if word2[idx] not in wordDict[ word1[idx] ]:
                        wordDict[ word1[idx] ].add(word2[idx])
                        indegree[ word2[idx] ] += 1
                    break

        res = []
        q = deque()
        for c in wordDict:
            if indegree[c] == 0:
                q.append(c)
        
        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in wordDict[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return "".join(res) if len(res) == len(wordDict) else ""
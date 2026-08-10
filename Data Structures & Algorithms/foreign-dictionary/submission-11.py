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
            
            for j in range(minLen):
                if word2[j] != word1[j]:
                    if word2[j] not in wordDict[word1[j]]:
                        wordDict[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        res = ""
        while q:
            curr = q.popleft()
            res += curr
            for nei in wordDict[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == len(indegree) else ""

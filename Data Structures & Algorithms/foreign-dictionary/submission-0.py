class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        graph = {c:set() for w in words for c in w}
        indegree = {c:0 for c in graph}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""
            
            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
            
        q = deque([])
        res = []
        for char in indegree:
            if indegree[char] == 0:
                q.append(char)
        
        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        if len(res) != len(indegree):
            return ""
        
        return "".join(res)


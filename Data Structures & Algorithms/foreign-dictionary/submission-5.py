class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # indegree topology
        graph = {c:set() for w in words for c in w}
        indegree = {c:0 for c in graph}

        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]

            minlen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minlen] == word2[:minlen]:
                return ""
            
            for j in range(minlen):
                # 遇到不一样的字母了， 找到第一个不一样的就要break，后面就不能作为参考了
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break
        
        q = deque([])
        res = []
        for c in graph:
            if indegree[c] == 0:
                q.append(c)

        while q:
            curr = q.popleft()
            res.append(curr)

            for nei in graph[curr]:
                indegree[nei]-=1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(res) if len(res) == len(indegree) else ""
            
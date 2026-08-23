class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        # indegree， topology sort
        orderDict = {c:set() for word in words for c in word}
        indegree = {c:0 for c in orderDict}

        for i in range(len(words)-1):
            first = words[i]
            second = words[i+1]

            minLen = min(len(first), len(second))
            if len(first) > len(second) and first[:minLen] == second[:minLen]:
                return ""
            
            for i in range(minLen):
                firstChar = first[i]
                secondChar = second[i]

                if firstChar == secondChar:
                    continue
                if secondChar not in orderDict[firstChar]:
                    orderDict[firstChar].add(secondChar)
                    indegree[secondChar] +=1
                break

        
        q = deque()
        for c in indegree:
            if indegree[c] == 0:
                q.append(c)
        
        res = ""
        while q:
            curr = q.popleft()
            res += curr
            for nei in orderDict[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == len(indegree) else ""

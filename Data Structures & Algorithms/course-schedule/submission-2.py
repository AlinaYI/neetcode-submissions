class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # indegree, dependency, topology sort
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for pre, course in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque()
        for c in range(numCourses):
            if indegree[c] == 0:
                q.append(c)
        res = 0
        while q:
            curr = q.popleft()
            res += 1
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return res == numCourses
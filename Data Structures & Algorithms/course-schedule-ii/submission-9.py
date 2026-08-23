class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0]*numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] +=1
        
        q = deque()
        for course, val in enumerate(indegree):
            if val == 0:
                q.append(course)
        
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        #indegree dependency, topology sort

        graph = defaultdict(list)
        indegree = [0]*numCourses
    
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
            
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for nei in graph[curr]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return res if len(res) == numCourses else []

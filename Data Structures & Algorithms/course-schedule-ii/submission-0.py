class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indegree_map = defaultdict(list)
        indegree = [0]*numCourses

        for course, pre in prerequisites:
            indegree_map[pre].append(course)
            indegree[course] += 1
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        res = []
        while q:
            pre = q.popleft()
            res.append(pre)

            for neigbor in indegree_map[pre]:
                indegree[neigbor] -= 1
            
                if indegree[neigbor] == 0:
                    q.append(neigbor)
        return res if len(res) == numCourses else []
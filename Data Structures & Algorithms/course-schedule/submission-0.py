class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        indegree_map = defaultdict(list)
        indegree = [0]*numCourses
        for course, prerequest in prerequisites:
            indegree_map[prerequest].append(course)
            indegree[course] += 1
        
        q = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        res = 0
        while q:
            pre = q.popleft()
            res += 1

            for course in indegree_map[pre]:
                indegree[course] -= 1

                if indegree[course] == 0:
                    q.append(course)
        
        return res == numCourses
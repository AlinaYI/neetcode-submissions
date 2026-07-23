class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        graph: = {pre: course}
        indegree  = [] 

        q = deque([])
        indegree 0 in our q
        [0, 2]

        traverse -- this q:
            neigbor in course
            indegree[neigbor] -= 1
            if indegree[neigbor] ? == 0 --> add q
        '''

        # topology sort, build graph
        graph = defaultdict(list)
        indegree = [0] *numCourses

        # graph = {[]}
        # indegree = [0, 0, 0]

        for course, prere in prerequisites:
            graph[prere].append(course)
            indegree[course] += 1
        
        # graph = {0: [1]}
        # indegree =  [0, 1, 0]
        
        q = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # q : [(0, 2)]

        res = []
        while q:
            pre = q.popleft()
            res.append(pre)
            # res = [0]

            for nei in graph[pre]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)
                    # q: [2, 1]
        return res if len(res) == numCourses else []
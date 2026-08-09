class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # eurliar path
        # stack[::-1]
        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse=True):
            graph[start].append(end)
        
        stack = ["JFK"]
        res = []
        while stack:
            curr = stack[-1]

            if graph[curr]:
                nextVisited = graph[curr].pop()
                stack.append(nextVisited)
            else:
                res.append(stack.pop())
        return res[::-1]
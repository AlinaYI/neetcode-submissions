class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # 欧拉path
        #  Hierholzer algo

        graph = defaultdict(list)
        for start, end in sorted(tickets, reverse = True):
            graph[start].append(end)
        
        stack = ["JFK"]
        res = []
        while stack:
            curr = stack[-1]

            if graph[curr]:
                next_place = graph[curr].pop()
                stack.append(next_place)
            else:
                res.append(stack.pop())

        return res[::-1]


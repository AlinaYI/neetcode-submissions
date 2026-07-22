class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for source, destination in sorted(tickets, reverse = True):
            graph[source].append(destination)

        res = []
        stack = ["JFK"]

        while stack:
            airport = stack[-1]

            if graph[airport]:
                next_airport = graph[airport].pop()
                stack.append(next_airport)
            else:
                res.append(stack.pop())
            
        return res[::-1]

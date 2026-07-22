class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        graph = defaultdict(list)

        for source, destination in sorted(tickets, reverse = True):
            graph[source].append(destination)

        res = []

        def dfs(airport):

            while graph[airport]:
                next_airport = graph[airport].pop()
                dfs(next_airport)
            
            res.append(airport)
        
        dfs("JFK")
        return res[::-1]
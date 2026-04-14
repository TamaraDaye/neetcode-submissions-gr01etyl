class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        tickets.sort(reverse = True)

        for src, dst in tickets:
            adj[src].append(dst)


        res = []

        def dfs(node):
            while adj[node]:
                next_node = adj[node].pop()
                dfs(next_node)

            res.append(node)

        dfs("JFK")
        return res[::-1]

        



        
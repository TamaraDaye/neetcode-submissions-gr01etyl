class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        min_stop = {}
        min_heap = [[0,src,-1]]


        for frm, to, cost in flights:
            adj[frm].append((to, cost))


        while min_heap:
            cost, node, stop = heapq.heappop(min_heap)
            
            if node == dst:
                return cost

            if stop == k:
                continue

            if node in min_stop and min_stop[node] <= stop:
                continue

            min_stop [node] = stop

            for v, cst in adj[node]:
                heapq.heappush(min_heap, [cst + cost, v, stop + 1])

        
        return -1
    
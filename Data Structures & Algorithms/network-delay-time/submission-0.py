class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)

        for edge in times:
            src, dst, cost = edge
            adj[src].append((dst, cost))

        
        shortest = {}
        min_heap = [[0, k]]


        while min_heap:
            cost, node = heapq.heappop(min_heap)

            if node in shortest:
                continue
            
            shortest[node] = cost

            for nd, cst in adj[node]:
                if nd not in shortest:
                    heapq.heappush(min_heap, [cst + cost, nd])


        return max(shortest.values()) if len(shortest) == n else -1




        
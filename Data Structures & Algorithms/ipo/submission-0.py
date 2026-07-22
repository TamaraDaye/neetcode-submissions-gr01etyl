class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        indices = list(range(n))
        indices.sort(key = lambda i: capital[i])

        profit, idx = [], 0

        for _ in range(k):
            while idx < n and capital[indices[idx]] <= w:
                heapq.heappush_max(profit,  profits[indices[idx]])
                idx += 1

            if not profit:
                break
            w += heapq.heappop_max(profit)

        return w


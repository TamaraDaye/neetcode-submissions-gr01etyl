class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        min_heap = [[0, 0, 0]]
        visit =set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        while min_heap:
            diff, r, c = heapq.heappop(min_heap)

            if (r,c) in visit:
                continue

            visit.add((r, c))


            if (r, c) == (ROWS - 1, COLS - 1):
                return diff


            for dr, dc in directions:
                xr, xc = r + dr, c + dc

                if xr < 0 or xc < 0 or xr >= ROWS or xc >= COLS or (xr, xc) in visit:
                    continue

                new_diff = max(diff, abs(heights[r][c] - heights[xr][xc]))
                heapq.heappush(min_heap, [new_diff, xr, xc])

        return 0

        
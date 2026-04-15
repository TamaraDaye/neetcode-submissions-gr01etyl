class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, v ,u):
        pv, pu = self.find(v), self.find(u)

        if pv == pu:
            return False

        if self.rank[pv] > self.rank[pu]:
            self.parents[pu] = pv
        
        elif self.rank[pu] > self.rank[pv]:
            self.parents[pv] = pu

        else:
            self.parents[pu] = pv
            self.rank[pv] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        uf = UnionFind(len(points))
        edges = []

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))

        edges.sort()
        res = 0
        for dist, u, v in edges:
            if uf.union(u, v):
                res += dist

        return res




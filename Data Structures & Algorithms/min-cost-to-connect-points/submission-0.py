class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                x1,y1 = points[i]
                x2,y2 = points[j]
                val = abs(x1-x2) + abs(y1-y2)
                adj[i].append([val,j])
                adj[j].append([val,i])
        minheap = [[0,0]]
        visit = set()
        res = 0
        while len(visit) < n:
            cost,point = heapq.heappop(minheap)
            if point in visit: continue
            visit.add(point)
            res += cost
            for neicost,nei in adj[point]:
                heapq.heappush(minheap,[neicost,nei])
        return res
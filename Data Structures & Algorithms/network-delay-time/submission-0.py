class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src,dst,time in times:
            adj[src].append((dst,time))
        minheap = [[0,k]]
        res = 0
        visit = set()
        while minheap:
            time,node = heapq.heappop(minheap)
            if node in visit: continue
            visit.add(node)
            res = max(res,time)
            for nei,neitime in adj[node]:
                heapq.heappush(minheap,[time+neitime,nei])
        return res if len(visit) == n else -1
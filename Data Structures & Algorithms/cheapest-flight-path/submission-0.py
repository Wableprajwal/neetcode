class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s,d,cost in flights:
            adj[s].append([d,cost])
        minheap = [[0,src,0]]
        prices = [float("inf")]*n
        prices[src] = 0
        while minheap:
            stops,src,cost = heapq.heappop(minheap)
            if stops > k: continue
            for nei,neicost in adj[src]:
                if cost + neicost < prices[nei]:
                    prices[nei] = cost + neicost
                    heapq.heappush(minheap,[stops+1,nei,prices[nei]])
        return prices[dst] if prices[dst] != float("inf") else -1
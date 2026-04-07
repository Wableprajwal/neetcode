class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        minheap = [[grid[0][0],0,0]]
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        while minheap:
            t,r,c = heapq.heappop(minheap)
            if (r,c) == (rows-1,cols-1): return t
            if (r,c) in visit: continue
            visit.add((r,c))
            for dr,dc in directions:
                nr,nc = r+dr,c+dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    heapq.heappush(minheap,[max(t,grid[nr][nc]),nr,nc])
        return -1

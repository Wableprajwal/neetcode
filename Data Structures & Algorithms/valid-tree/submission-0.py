class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        premap = {i:[] for i in range(n)}
        for x,y in edges:
            premap[x].append(y)
            premap[y].append(x)
        visited,cycle = set(),set()

        def dfs(i,prev):
            if i in cycle: return False
            cycle.add(i)
            for j in premap[i]:
                if j == prev: continue
                if not dfs(j,i): return False
            cycle.remove(i)
            visited.add(i)
            return True
        
        return dfs(0,-1) and n == len(visited)

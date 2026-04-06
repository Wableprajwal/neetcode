class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        premap = {i:[] for i in range(n)}
        for u,v in edges:
            premap[u].append(v)
            premap[v].append(u)
        visited = set()
        def dfs(i):
            if i in visited: return 
            visited.add(i)
            for j in premap[i]:
                dfs(j)
        
        res = 0
        for i in range(n):
            if i not in visited:
                res +=1
                dfs(i)
        return res
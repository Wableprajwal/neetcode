class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}
        visited = set()
        for src,dst in edges:
            adj[src].append(dst)
            adj[dst].append(src)
        
        def dfs(src,prev):
            if src in visited: return False
            visited.add(src)
            for dst in adj[src]:
                if dst == prev: continue
                if not dfs(dst,src): return False
            return True
        
        return dfs(0,-1) and len(visited) == n

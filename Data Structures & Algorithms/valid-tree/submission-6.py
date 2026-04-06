class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        visit = set()
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node,prev):
            if node in visit: return False
            visit.add(node)
            for dst in adj[node]:
                if dst == prev: continue
                if not dfs(dst,node): return False
            return True
        
        return dfs(0,-1) and len(visit) == n
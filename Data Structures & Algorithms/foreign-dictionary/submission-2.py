class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:[] for w in words for c in w}
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: return ""
            for c in range(minlen):
                if w1[c] != w2[c]:
                    adj[w1[c]].append(w2[c])
                    break
        print(adj.items())
        visit,cycle = set(),set()
        res = []
        def dfs(c):
            nonlocal res
            if c in cycle: return False
            if c in visit: return True
            cycle.add(c)
            for nei in adj[c]:
                if not dfs(nei): return False
            visit.add(c)
            cycle.remove(c)
            res.append(c)
            return True
        
        for c in adj:
            if not dfs(c): return ""
        return "".join(res[::-1])
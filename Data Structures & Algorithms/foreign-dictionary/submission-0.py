import collections
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit,cycle = set(),set()
        res = []
        def dfs(ch):
            if ch in visit: return True
            if ch in cycle: return False
            cycle.add(ch)
            for nei in adj[ch]:
                if nei not in visit:
                    if not dfs(nei): return False
            cycle.remove(ch)
            visit.add(ch)
            res.append(ch)
            return True
        
        for c in adj:
            if not dfs(c): return ""
        return "".join(res[::-1])
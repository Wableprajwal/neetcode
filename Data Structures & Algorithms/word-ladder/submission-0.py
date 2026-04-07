class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pat = word[:i] + '*' + word[i+1:]
                adj[pat].append(word)
        visit = set()
        visit.add(beginWord)
        q = deque()
        q.append(beginWord)
        res = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord: return res
                for i in range(len(word)):
                    pat = word[:i] + '*' + word[i+1:]
                    for nei in adj[pat]:
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1
        return 0
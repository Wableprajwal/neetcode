class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        endidx = {}
        for i,c in enumerate(s):
            endidx[c] = i
        start,end = 0,0
        size = 1
        res = []
        while start < len(s):
            if endidx[s[start]] > end:
                end = endidx[s[start]]
            if start == end:
                res.append(size)
                size = 0
            size +=1
            start +=1
        return res
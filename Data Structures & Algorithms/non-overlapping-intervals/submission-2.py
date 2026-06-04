class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevend = intervals[0][1]
        res = 0
        for start,end in intervals[1:]:
            if prevend <= start: prevend = end
            else:
                prevend = min(prevend,end)
                res +=1
        return res
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res,count = 0,0
        i,j = 0,0
        while i < len(start):
            if start[i] < end[j]:
                i+=1
                count+=1
            else:
                j+=1
                count-=1
            res = max(res,count)
        return res
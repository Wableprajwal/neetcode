class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        unused = [i for i in range(n)]
        used = []
        count = [0]*n
        for start, end in meetings:
            while used and used[0][0] <= start:
                _,room = heapq.heappop(used)
                heapq.heappush(unused,room)
            if not unused:
                end_time,room = heapq.heappop(used)
                end = end_time + (end - start)
                heapq.heappush(unused,room)
            room = heapq.heappop(unused)
            heapq.heappush(used,(end,room))
            count[room] += 1
        return count.index(max(count))
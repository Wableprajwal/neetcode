class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        minheap, res = [],[]
        i = 0
        time = tasks[0][0]
        while minheap or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(minheap,(tasks[i][1],tasks[i][2]))
                i+=1
            if minheap:
                pro_t, idx = heapq.heappop(minheap)
                time += pro_t
                res.append(idx)
            else:
                time = tasks[i][0]
        return res
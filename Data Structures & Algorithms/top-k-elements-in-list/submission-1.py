class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        res = []
        for n,f in count.items():
            freq[f].append(n)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                k-=1
                if k ==0: return res
        return res
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        cur = 0
        for n in nums:
            cur = max(n,cur + n)
            res = max(res,cur)
        return res
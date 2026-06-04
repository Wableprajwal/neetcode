class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dp = {}
        dp[0] = 1
        cur,res = 0,0
        for n in nums:
            cur += n
            diff = cur - k
            if diff in dp:
                res += dp[diff]
            if cur not in dp:
                dp[cur] =1
            else:
                dp[cur] +=1
        return res
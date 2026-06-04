class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        dp = {}
        res = 0
        while r < len(s):
            if s[r] in dp:
                l = max(l,dp[s[r]]+1)
            dp[s[r]] = r
            res = max(res,r-l+1)
            r+=1
        return res

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        for r in range(len(word1)):
            dp[r][len(word2)] = len(word1)-r
        for c in range(len(word2)):
            dp[len(word1)][c] = len(word2)-c
        for r in range(len(word1)-1,-1,-1):
            for c in range(len(word2)-1,-1,-1):
                if word1[r] == word2[c]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1 + min(dp[r+1][c],dp[r][c+1],dp[r+1][c+1])
        return dp[0][0]
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows,cols = len(matrix),len(matrix[0])
        dp = {}
        def dfs(r,c,prev):
            if 0 <= r < rows and 0 <= c < cols and matrix[r][c] > prev:
                if (r,c) in dp: return dp[(r,c)]
                dp[(r,c)] = max(1+dfs(r+1,c,matrix[r][c]),
                                1+dfs(r-1,c,matrix[r][c]),
                                1+dfs(r,c+1,matrix[r][c]),
                                1+dfs(r,c-1,matrix[r][c]))
                return dp[(r,c)]
            else:
                return 0
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,-1)
        return max(dp.values())

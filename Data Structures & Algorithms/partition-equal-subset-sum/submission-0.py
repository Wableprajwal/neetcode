class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 : return False
        target = sum(nums)//2
        dp = {}
        def dfs(i,total):
            if total == target:
                return True
            if total > target or i == len(nums):
                return False
            if (i,total) in dp: return dp[(i,total)]
            res = dfs(i+1,total) or dfs(i+1,total + nums[i])
            dp[(i,total)] = res
            return res
        return dfs(0,0)
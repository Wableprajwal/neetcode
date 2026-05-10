class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dp = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in dp:
                return [dp[diff],i]
            dp[n] = i
        return []
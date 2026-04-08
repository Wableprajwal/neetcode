class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr(nums):
            rob1,rob2 = 0,0
            for n in nums[::-1]:
                tmp = max(rob1,n+rob2)
                rob2 = rob1
                rob1 = tmp
            return rob1
        return max(hr(nums[1:]),hr(nums[:-1]),nums[0])

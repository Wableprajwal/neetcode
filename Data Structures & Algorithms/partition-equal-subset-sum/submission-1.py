class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 != 0 : return False
        target = sum(nums)//2
        dp = set()
        dp.add(0)
        for n in nums:
            newdp = dp.copy()
            for j in dp:
                newdp.add(j+n)
            dp = newdp
        return True if target in dp else False
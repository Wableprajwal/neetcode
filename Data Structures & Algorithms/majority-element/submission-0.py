class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for n in nums:
            if count == 0:
                val = n
            count += (1 if n == val else -1)
        return val
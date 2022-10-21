class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
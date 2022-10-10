class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val:index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

s1 = Solution()
print(s1.twoSum([1,2,3,1], 5))

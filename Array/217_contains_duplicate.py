class Solution:
        def containsDuplicate(self, nums: list[int]) -> bool:
                hashset = set()

                for i in nums:
                        if i in hashset:
                                return True
                        hashset.add(i)
                return False

s1 = Solution()
l1 = [1,2,3,1]
print(s1.containsDuplicate(l1))



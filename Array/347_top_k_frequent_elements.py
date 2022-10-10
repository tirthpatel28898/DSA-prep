class Solution:
    def topKFrequent(self,nums: list[int], k: int) -> list[int]:
        count = {} # hashmap to count occurance
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # default 0 if n does not exist in our hashmap
        for n, c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, 0, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        # O(n)
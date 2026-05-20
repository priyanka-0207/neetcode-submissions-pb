class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            bucket[count].append(num)
        for j in range(len(bucket)-1, -1, -1):
            for num in bucket[j]:
                res.append(num)
                if len(res) == k:
                    return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)] # O(n)

        counter = {}
        for n in nums: # O(n)
            counter[n] = counter.get(n, 0) + 1

        for key, val in counter.items():
            bucket[val].append(key)

        result = []
        for n in reversed(bucket):
            if n:
                result.extend(n)
                k -= len(n)
            if k == 0:
                break

        return result

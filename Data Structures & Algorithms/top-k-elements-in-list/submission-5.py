class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        solutions = [[] for _ in range(len(nums) + 1)]

        for n, v in counter.items():
            solutions[v].append(n)


        i = len(solutions) - 1
        result = []
        for i in range(len(solutions) - 1, 0, -1):
            for s in solutions[i]:
                result.append(s)
                if len(result) == k: return result
        
        return result

# 1, 2, 1, 3
# {1: 2, 2: 1, 3: 1}
# [0, 0, 0, 0] -> [0, 3, 1, 0]
# result = [1, 3]

# 1, 2, 2, 3, 3, 3
# {1: 1, 2: 2, 3: 3}
# [0, 0, 0, 0, 0, 0] -> [0, 1, 2, 3, 0, 0]
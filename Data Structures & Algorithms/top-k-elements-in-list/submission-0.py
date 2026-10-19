class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums: # O(n)
            if n in counter:
                counter[n] += 1
            else:
                counter[n] = 1
        
        l = list(counter.items())
        
        l = sorted(l, key=lambda x: x[1], reverse=True) # O k log(k)

        return [ll[0] for ll in l[:k]]

# [1, 2, 3, 2, 3, 3]
# {1: 1, 2: 2, 3:, 3}
# [[1, 1], [2, 2], [3, 3]]
# [[3, 3], [2, 2], [1, 1]]
# return [3, 2]

# [1, 1]
# {1: 2}
# [[1, 2]]
# [[1, 2]]
# return [1]
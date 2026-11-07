
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sys.setrecursionlimit(100_000)
        unique = dict()
        for n in nums:	# O(n)
            unique[n] = None

        maxx = 0
        for n in unique:
            score = self.recur(n, unique)
            maxx = max(maxx, score)

        return maxx


    def recur(self, curr, unique):
        rest = 0
        
        if curr in unique:
            if unique[curr]:
                rest = unique[curr]
            else:
                rest = self.recur(curr + 1, unique) + 1
            unique[curr] = rest
        return rest	

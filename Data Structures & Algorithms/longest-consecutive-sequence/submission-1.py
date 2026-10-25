class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique = set()
        for n in nums:
            unique.add(n)
        
        starts = set()
        for n in unique:
            if n-1 not in unique:
                starts.add(n)
        
        maxx = 1
        i = 1
        for s in starts:
            while True:
                if s + i in unique:
                    i += 1
                    maxx = max(maxx, i)
                else:
                    i = 1
                    break
        
        return maxx
        

# {1, 0, 2, 6, 2, 4, 5, 7}
# unique {0, 1, 2, 4, 5, 6, 7}
# starts {0, 4}
# 0 -++-> 1 -++> 2 maxx = 3
# 4 -++-> 5 -++-> 6 -++-> 7 maxx = 4

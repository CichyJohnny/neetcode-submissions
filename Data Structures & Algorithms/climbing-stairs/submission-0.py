class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [None for _ in range(n + 1)]

        def climb(n):
            if n == 0:
                return 1

            if cache[n] is not None:
                return cache[n]
            
            a = climb(n - 1)
            if n >= 2: a += climb(n - 2)

            cache[n] = a

            return a
        
        return climb(n)

# 3
# a) 3-1=2
# b) 3-2=1
# aa) 2-1=1
# aa) 2-2=0, return 1
# aaa) 1-1=0, return 1
# bb) 1-1=0, return 1
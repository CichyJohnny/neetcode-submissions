class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minsteps = [None for _ in range(len(cost))]

        def step(i):
            if i >= len(cost):
                return 0

            if minsteps[i] is not None:
                return minsteps[i]
            
            step1 = step(i + 1)
            step2 = step(i + 2)

            minsteps[i] = cost[i] + min(step1, step2)
            return minsteps[i]
            
        return min(step(0), step(1))

# [1,2,1,2,1,1,1]
# - step(6, 0+1)
# -1 step(5, 1+1)
# -2 step(4, 1+1)
# -1-1 step(4, 2+1)
# -1-1-1 step(3, 3+2)
# -1-1-1-1 step(2, 5+1)
# -1-1-1-2 step(1, 5+2) return 7
# -1-1-1-1-1 step(1, 6+2) return 8
# -1-1-1-1-2 step(0, 6+1) return 7

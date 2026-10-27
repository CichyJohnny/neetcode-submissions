class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right = [0 for _ in range(len(prices))]
        maxx = 0

        for i in range(len(prices) - 2, -1, -1):
            curr_max_right = max(prices[i + 1], max_right[i + 1])
            max_right[i] = curr_max_right
            maxx = max(curr_max_right - prices[i], maxx)

        
        return max(maxx, 0)

# [10,1,5,6,7,1]
# [7,7,7,7,1,0]
# [-3,6,2,1,-6,-1], maxx=6

# [10,8,7,5,2]
# [8,7,5,2,0]
# [-2,-1,-2,-3,-2]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        result = 0

        for i in reversed(range(len(prices))):
            result = max(result, best - prices[i])

            best = max(best, prices[i])
        
        return result
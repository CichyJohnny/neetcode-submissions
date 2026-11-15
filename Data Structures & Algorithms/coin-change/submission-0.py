class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.amount = amount
        self.coins = coins

        self.cache = [None for _ in range(amount)]

        result = self.goup(0)
        if result == float("inf"):
            return -1
        return result

    def goup(self, i):
        if i > self.amount:
            return float("inf")
        if i == self.amount:
            return 0
        if self.cache[i]:
            return self.cache[i]
        
        cost = 1 + min(self.goup(i + n) for n in self.coins)
        self.cache[i] = cost
        return cost
        

from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        p = max(piles)

        while l < p:
            mid = (l + p) // 2

            time = self.measure(piles, mid)

            if time <= h:
                p = mid
            else:
                l = mid + 1
        
        return l
    
    def measure(self, piles, rate):
        return sum(ceil(p / rate) for p in piles)

# piles = [1,4,3,2], h = 9
# l=1, p=4, mid=2, time=6 < 9
# l=1, p=2, mid=1, time=10 > 9
# l=2, p=2, mid=2, time=6 < 9
# return 2

# piles = [25,10,23,4], h = 4
# l=1, p=25, mid=13, time=6 > 4
# l=14, p=25, mid=19, time=6 > 4
# l=20, p=25, mid=22, time=6 > 4
# l=23, p=25, mid=24, time=5 > 4
# l=25, p=25, mid=24, time=4 == 4
# return 24

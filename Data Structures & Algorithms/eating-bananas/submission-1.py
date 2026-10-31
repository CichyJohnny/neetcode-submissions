from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()

        l = 1
        p = max(piles)
        
        minn=float("inf")
        while l <= p:
            i = (l + p) // 2
            t = self.calcTime(piles, i)
            if t > h:
                l = i + 1
            else:
                p = i - 1
                minn = min(minn, i)
        
        return minn
    
    def calcTime(self, piles, k):
        return sum([ceil(n / k) for n in piles])
        
# [1,4,3,2], h=9
# [1,4,3,2], l=1, p=4, i=2, calcTime(2)=6<9
# [1,4,3,2], l=1, p=1, i=1, calcTime(1)=10>9
# return 2

# [25,10,23,4], h=4
# [25,10,23,4], l=1, p=25, i=13, calcTime(13)=6>4
# [25,10,23,4], l=14, p=25, i=19, calcTime(19)=6>4
# [25,10,23,4], l=20, p=25, i=22, calcTime(22)=6>4
# [25,10,23,4], l=23, p=25, i=24, calcTime(24)=5>4
# [25,10,23,4], l=25, p=25, i=24, calcTime(25)=4==4
# return 25

# [1000000000,1,1], h=5
# [1000000000,1,1], l=1, p=1000000000, i=500000000, calcTime(500000000)=4<5
# [1000000000,1,1], l=1, p=499999999, i=250000000, calcTime(250000000)=6>5
# [1000000000,1,1], l=250000001, p=499999999, i=375000000, calcTime(375000000)=5==5

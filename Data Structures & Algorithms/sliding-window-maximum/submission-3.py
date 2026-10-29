from heapq import heappop, heappush, heapify

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h = []
        heapify(h)


        for i in range(k):
            heappush(h, (-nums[i], i))
        
        results = []
        results.append(-h[0][0])

        for i in range(k, len(nums)):
            while h and h[0][1] <= i - k:
                heappop(h)
            
            heappush(h, (-nums[i], i))
            results.append(-h[0][0])
        
        return results

# 3 3 3 3 1

# [1,2,1,0,4,2,6] k=3
# [1,2,1] h=[2,1,1] removed={} results=[2]
# [2,1,0] h=[2,1,1,0] removed={1} results=[2,2]
# [1,0,4] h=[4,2,1,1,0] removed={1,2} results=[2,2,4]
# [0,4,2] h=[4,2,2,1,1,0] removed={1,2} results=[2,2,4,4]
# [4,2,6] h=[6,2,1,1,0] removed={1,2,0} results=[2,2,4,4,6]
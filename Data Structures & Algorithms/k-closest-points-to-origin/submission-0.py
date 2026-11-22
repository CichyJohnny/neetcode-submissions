from heapq import heapify, heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapify(heap)

        for x, y in points:
            d = x**2 + y**2
            heappush(heap, (-d, x, y))

            if len(heap) > k:
                heappop(heap)

        
        result = []
        for _ in range(k):
            _, x, y = heappop(heap)
            result.append([x, y])
        
        return list(reversed(result))

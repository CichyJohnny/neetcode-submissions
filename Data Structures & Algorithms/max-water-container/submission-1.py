class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxx = 0
        while l < r:
            v = (r - l) * min(heights[l], heights[r])

            maxx = max(maxx, v)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxx

# [1,7,2,5,4,7,3,6]
# 7 - 0 * Min(1,6) = 7*1=7
# 7-1 * min(7,6) = 36
# 6-1 * min(7,3) = 15
# 5-1 * min(7,7) = 28
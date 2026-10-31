class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxx = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                p = stack.pop()
                l = stack[-1] if stack else -1
                area = (i - l - 1) * heights[p]
                maxx = max(maxx, area)
            stack.append(i)
        
        while stack:
            p = stack.pop()
            l = stack[-1] if stack else -1
            area = (len(heights) - l - 1) * heights[p]
            maxx = max(maxx, area)
        
        return maxx

# heights=[7,1,7,2,2,4]
# 7, stack=[(0,7)]
# 1, stack=[(1,1)], p=1, l=0, 7*(1-0)
# 7, stack=[(1,1),(2,7)]
# 2, stack=[(1,1),(3,2)], p=3, l=2, 7*(3-2)
# 2, stack=[(1,1),(3,2),(4,2)]
# 4, stack=[(1,1),(3,2),(4,2),(5,4)]
# 0, stack=[(1,1),(3,2),(4,2)], p=6, l=4, 4*(6-4-§)
# 0, stack=[(1,1),(3,2)], p=6, l=3, 2*(6-3-1)
# 0, stack=[(1,1)], p=6, l=1, 2*(6-1-1)
# 0, stack=[], p=6, l=-1, 1*(6-(-1)-1)

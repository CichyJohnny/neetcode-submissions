class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights: return 0

        stack = []
        maxx = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                p = stack.pop()
                l = stack[-1] if stack else -1

                area = heights[p] * (i - l - 1)
                maxx = max(maxx, area)
            
            stack.append(i)
        
        last = len(heights) - 1
        while stack:
                p = stack.pop()
                l = stack[-1] if stack else -1

                area = (last - l) * heights[p]
                maxx = max(maxx, area)
        
        return maxx

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        result = 0

        while left < right:
            height = min(heights[left], heights[right])
            volume = (right - left) * height

            result = max(result, volume)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return result

# [1,7,2,5,4,7,3,6]
# 1, 6 -> v=7*min(1,6)=7, result=7, 1<6
# 7, 6 -> v=6*min(7,6)=36, result=36, 7>=6
# 7, 3 -> v=5*min(7,3)=15, result=36, 7>=3
# 7, 7 -> v=4*min(7,7)=28, result=36, 7>=7
# 7, 4 -> v=3*min(7,4)=12, result=36, 7>=4
# 7, 5 -> v=2*min(7,5)=10, result=36, 7>=5
# 7, 2 -> v=1*min(7,2)=2, result=36

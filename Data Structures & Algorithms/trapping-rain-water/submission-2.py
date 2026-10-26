class Solution:
    def trap(self, height: List[int]) -> int:
        preff = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            preff[i] = max(preff[i - 1], height[i - 1])
        
        suff = [0 for _ in range(len(height))]
        for i in range(len(height) - 2, -1, -1):
            suff[i] = max(suff[i + 1], height[i + 1])
        
        result = 0
        for i in range(len(height)):
            point = min(preff[i], suff[i]) - height[i]
            if point > 0:
                result += point
        
        return result

# [0,2,0,3,1,0,1,3,2,1]
# preff = [0,0,2,2,3,3,3,3,3,3]
# suff  = [3,3,3,3,3,3,3,2,1,0]
# 0 -> min(0,3) - 0, result = 0
# 2 -> min(0,3) - 2, result = 0
# 0 -> min(2,3) - 0, result = 2
# 3 -> min(2,3) - 3, result = 2
# 1 -> min(3,3) - 1, result = 4
# 0 -> min(3,3) - 0, result = 7
# 1 -> min(3,3) - 1, result = 9
# 3 -> min(3,2) - 3, result = 9
# 2 -> min(3,1) - 2, result = 9
# 1 -> min(3,0) - 1, result = 9

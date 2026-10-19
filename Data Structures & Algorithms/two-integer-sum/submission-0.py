class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            if n in seen:
                found = seen[n]
                return [min(i, seen[n]), max(i, seen[n])]

            seen[target - n] = i
        
        return []
    
# [3,4,5,6] 7
# 7-3=4 {4: 0}, 4 in {4:0}, return [0, 1]
# [1,1,-2] -1
# -1-1=-2 {-2: 0}, -1-1=-2 {-2: 1}, -2 in {-2: 1}, return [1, 2]
# [0,0] 0
# 0-0=0 {0: 0}, 0 in {0: 0}, return [0, 1]

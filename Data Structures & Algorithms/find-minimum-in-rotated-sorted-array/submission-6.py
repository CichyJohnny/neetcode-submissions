class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return min(nums)
        if nums[0] < nums[-1]:
            return nums[0]

        l = 0
        p = len(nums) - 1
        
        while l <= p:
            i = (l + p) // 2

            if nums[i] < nums[(i-1) % len(nums)]:
                return nums[i]
            elif nums[p] < nums[i]:
                l = i + 1
            else:
                p = i
        
        return -1

# [5,6,7,8,9,3,4], l=0, p=6, i=3, 5>4 
# [5,6,7,8,9,3,4], l=5, p=6, i=6, 3<4
# [5,6,7,8,9,3,4], l=5, p=5, i=5, 3<9

# [9,-5,-2,0,3], l=0, p=4, i=2, 9>3
# [9,-5,-2,0,3], l=3, p=4, i=2, 0>3

# [4,5,6,7,0,1,2], l=0, p=6, i=3, 4<7
# [4,5,6,7,0,1,2], l=4, p=6, i=5, 7>0
# [4,5,6,7,0,1,2], l=4, p=4, i=4, 7>0

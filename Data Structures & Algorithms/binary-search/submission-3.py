class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        p = len(nums) - 1
        
        while l <= p:
            i = (l + p) // 2
            if nums[i] == target:
                return i
            elif nums[i] < target:
                l = i + 1
            else:
                p = i - 1
        
        return -1

# [-1,0,2,4,6,8], target = 4
# [-1,0,2,4,6,8], l=0, p=5, i=2, 2<4
# [-1,0,2,4,6,8], l=3, p=5, i=4, 6>4
# [-1,0,2,4,6,8], l=3, p=3, i=3, 4==4
# return 3

# [-1,0,2,4,6,8], target = 3
# [-1,0,2,4,6,8], l=0, p=5, i=2, 2<3
# [-1,0,2,4,6,8], l=3, p=5, i=4, 6>3
# [-1,0,2,4,6,8], l=3, p=3, i=3, 4>3
# [-1,0,2,4,6,8], l=3, p=2, l>p
# return -1

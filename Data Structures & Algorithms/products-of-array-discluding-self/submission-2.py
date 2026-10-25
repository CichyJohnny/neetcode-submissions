class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preff = [1]
        for i in range(1, len(nums)):
            preff.append(preff[-1] * nums[i - 1])
        suff = [1]
        for i in range(len(nums) - 2, -1, -1):
            suff.append(suff[-1] * nums[i + 1])
        
        return [preff[i] * suff[len(suff) - 1 - i] for i in range(len(nums))]

        


# [1, 2, 3, 4, 5]
# prefix [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4]]
# prefix_product [1, 1, 2, 6, 24]
# suffix [[2, 3, 4, 5], [3, 4, 5], [4, 5], [5], []]
# suffix_product [120, 60, 20, 5, 1]
# result [1*120, 1*60, 2:20, 6*5, 24*1]

# [1, 2, 4, 6]
# [[], [1], [1, 2], [1, 2, 4]]
# [1, 1, 2, 8]
# [[2, 4, 6], [4, 6], [6], []]
# [48, 24, 6, 1]
# [1*48, 1*24, 2*6, 8*1]

# [1, 0, 4, 6]
# [[], [1], [1, 0], [1, 0, 4]]
# [1, 1, 0, 0]
# [[0, 4, 6], [4, 6], [6], []]
# [0, 24, 6, 1]
# [1*0, 1*24, 0*6, 0*1]

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        triplets = set()
        for i in range(len(nums) - 2):
            results = self.twoSum(nums[(i+1):], -nums[i])
            for r in results:
                triplets.add(tuple([nums[i], r[0], r[1]]))
        
        return list(triplets)


    def twoSum(self, nums, target):
        left = 0
        right = len(nums) - 1

        results = set()

        while left < right:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                results.add(tuple([nums[left], nums[right]])) 
                left += 1
                right -= 1
        
        return list(results)


# [-1,0,1,2,-1,-4]
# [-4,-1,-1,0,1,2]
# 2sum [-1,-1,0,1,2] 4 -> []
# 2sum [-1,0,1,2] 1 -> [-1, 2] -> [0, 1] -> [[-1, -1, 2], [-1, 0, 1]]
# 2sum [0,1,2] 1 -> [0, 1] -> [[-1, 0, 1]]
# 2sum [1,2] 0 -> []
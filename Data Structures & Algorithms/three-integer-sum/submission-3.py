class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(n log n)

        # O(n^2)

        results = set()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if -nums[i] < nums[l] + nums[r]:
                    r -= 1
                elif -nums[i] > nums[l] + nums[r]:
                    l += 1
                else:
                    if l != r:
                        results.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1

        return list(list(r) for r in results)

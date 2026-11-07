class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_target = {}
        for i in range(len(nums)):
            to_target[target-nums[i]] = i

        for i in range(len(nums)):
            if nums[i] in to_target:
                j = to_target[nums[i]]
                if i != j:
                    return [min(i,j), max(i,j)]
        return []

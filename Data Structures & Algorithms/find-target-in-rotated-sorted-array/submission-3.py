class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l = 0
        p = len(nums) - 1
        result = -1
        if nums[0] < nums[-1]:
            result = 0
        else:
            while l <= p:
                i = (l + p) // 2

                if nums[i] < nums[(i-1) % len(nums)]:
                    result = i
                    break
                elif nums[p] < nums[i]:
                    l = i + 1
                else:
                    p = i

        l = result
        p = result + len(nums) - 1
        while l<=p:
            i = (l + p) // 2
            ii = i % len(nums)

            if nums[ii] == target:
                return ii
            elif nums[ii] < target:
                l = i + 1
            else:
                p = i - 1
        
        return -1

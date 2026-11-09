class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [None for _ in range(len(nums))]

        def step(i):
            if i >= len(nums):
                return 0
            
            if cache[i] is not None:
                return cache[i]

            step2 = step(i + 2)
            step3 = step(i + 3)

            cache[i] = nums[i] + max(step2, step3)
            return cache[i]
        
        return max(step(0), step(1))



class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        cache1 = [None for _ in range(len(nums) - 1)]
        cache2 = [None for _ in range(len(nums))]

        def step(i, cache):
            if i >= len(cache):
                return 0
            
            if cache[i] is not None:
                return cache[i]

            step2 = step(i + 2, cache)
            step3 = step(i + 3, cache)

            cache[i] = nums[i] + max(step2, step3)
            return cache[i]
        
        return max(step(0, cache1), step(1, cache1), step(1, cache2), step(2, cache2))

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            nl = numbers[left]
            nr = numbers[right]

            if target - nl - nr < 0:
                right -= 1
            elif target - nl - nr > 0:
                left += 1
            else:
                return [left + 1, right + 1]
        
        return []

# [1, 2, 3, 5] 5
# l=0, r=3, 5 - 1 - 5 = -1, -1 < 0
# l=0, r=2, 5 - 1 - 3 = 1, 1 > 0
# l=1, r=2, 5 - 2 - 3 = 0, 0 == 0, [1, 2]

# [1, 2, 3] 6
# l=0, r=2, 6 - 1 - 3 = 2, 2 > 0
# l=1, r=2, 6 - 2 - 3 = 1, 1 > 0
# 1 == 2, return [] (but description states it should always exist)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:	
            if target < numbers[l] + numbers[r]:
                r -= 1
            elif target > numbers[l] + numbers[r]:
                l += 1
            else:
                return [l + 1, r + 1]

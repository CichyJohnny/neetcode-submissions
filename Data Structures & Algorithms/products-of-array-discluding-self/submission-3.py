class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1]
        for i in range(1, len(nums)):
            add = prefixes[-1] * nums[i - 1]
            prefixes.append(add)

        # [1, 2, 4, 6]
        # prefixes = [1], nums[1:] = [2, 4, 6]
        # 2 -> prefixes = [1, 1*1]
        # 4 -> prefixes = [1, 1, 1*2]
        # 6 -> prefixes = [1, 1, 2, 2*4]

        sufixes = [1]
        for i in reversed(range(0, len(nums) - 1)):
            add = sufixes[-1] * nums[i + 1]
            sufixes.append(add)

        sufixes = list(reversed(sufixes))
        # [1, 2, 4, 6]
        # sufixes = [1], nums[:-1] = [1, 2, 4]
        # 4 -> sufixes = [1, 1*6]
        # 2 -> sufixes = [1, 6, 6*4]
        # 1 -> sufixes = [1, 6, 24, 24*2]
        # sufixes = [48, 24, 6, 1]

        # result [48*1, 24*1, 2*6, 8*1]


        return [prefixes[i] * sufixes[i] for i in range(len(nums))]

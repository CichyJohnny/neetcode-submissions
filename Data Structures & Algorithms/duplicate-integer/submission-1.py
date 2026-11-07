class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupp = set()
        for n in nums:
            if n in dupp:
                return True
            dupp.add(n)
        return False
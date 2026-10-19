class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        char_set = set()
        for n in nums: # O(N)
            if n in char_set:
                return True
            char_set.add(n)
        return False

        # [1, 2, 3, 3,]
        # 1 {1}
        # 2 {1, 2}
        # 3 {1, 2, 3}
        # 3 in {1, 2, 3}, return False
        
        # [1, 2, 3]
        # 1 {1}
        # 2 {1, 2}
        # 3 {1, 2, 3}
        
        # []
        # return True

        # [1, 1, 1]
        # 1 {1}
        # 1 in {1}, return False

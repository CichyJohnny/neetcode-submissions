class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = -float("inf")
        last_max = 1
        last_min = 1

        for n in nums:
            tmp_max = last_max
            last_max = max(
                n * last_max, # multyplying by last max subsequence
                n * last_min, # multyplying by last min subsequence (minus times minus)
                n             # starting new sequence
            )
            last_min = min(
                n * tmp_max, 
                n * last_min, 
                n
            )
            
            maxx = max(maxx, last_max)
        
        return maxx

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while not (s[left].isalpha() or s[left].isnumeric()):
                if left + 1 < right:
                    left += 1
                else:
                    return True
            
            while not (s[right].isalpha() or s[right].isnumeric()):
                if right - 1 > left:
                    right -= 1
                else:
                    return True
            
            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1
        
        return True



# aba
# [0, 2] a == a, True
# abba
# [0, 3] a == a, [1, 2] b == b, True
# a baba
# [0, 5] a == a, [1, 4], [2, 4] b == b, True 
# a   ba
# [0, 5] a == a, [1, 4], [2, 4], [3, 4], True
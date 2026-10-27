class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = dict()
        for s in s1:
            s1_counter[s] = s1_counter.get(s, 0) + 1
        
        s2_counter = dict()
        for s in s2[:len(s1) - 1]:
            s2_counter[s] = s2_counter.get(s, 0) + 1
        
        for i in range(len(s2) - len(s1) + 1):
            right_border = s2[i + len(s1) - 1]
            s2_counter[right_border] = s2_counter.get(right_border, 0) + 1

            if s1_counter == s2_counter:
                return True
            
            left_border = s2[i]
            if s2_counter[left_border] - 1 == 0:
                s2_counter.pop(left_border)
            else:
                s2_counter[left_border] = s2_counter.get(left_border) - 1
            
            
        
        return False


# abc lecabee
# lec abee, {l: 1, e: 1, c: 1} ?= {a: 1, b: 1, c: 1}
# l eca bee, {e: 1, c: 1, a: 1} ?= {a: 1, b: 1, c: 1}
# le cab ee, {c: 1, a: 1, b: 1} ?= {a: 1, b: 1, c: 1} True

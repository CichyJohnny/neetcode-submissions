class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        p = 0

        s1_count = {}
        for s in s1:
            s1_count[s] = s1_count.get(s, 0) + 1
        
        
        s2_count = {s2[0]: 1}

        while p < len(s2):
            print(s2_count)

            if not self.contain(s2_count, s1_count):
                p += 1
                if p < len(s2): s2_count[s2[p]] = s2_count.get(s2[p], 0) + 1
            else:
                if s1_count != s2_count:
                    s2_count[s2[l]] -= 1
                    if s2_count[s2[l]] == 0: s2_count.pop(s2[l])
                    l += 1
                else:
                    return True
            
        return False

    def contain(self, d1, d2):
        for k, v in d2.items():
            if k not in d1: return False
            if v > d1[k]: return False
        return True

# s1 = "abc", s2 = "lecabee"
# l, contain=False
# le, contain=False
# lec, contain=False
# leca, contain=False
# lecab, contain=True, equal=False
# ecab, contain=True, equal=False
# cab, contain=True, equal=True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        p = 0

        counter = {}
        for tt in t:
            counter[tt] = counter.get(tt, 0) + 1
        
        shortest = ()
        length = float("inf")
        expand = True
        while p <= len(s):
            if zerosDict(counter):
                sub = s[l:p]
                if len(sub) < length:
                    shortest = (l, p)
                    length = p - l + 1
                
                if s[l] in counter:
                    counter[s[l]] = counter[s[l]] + 1

                l += 1
            else:
                if p == len(s):
                    break
                
                if s[p] in counter:
                    counter[s[p]] = counter[s[p]] - 1
                p += 1

        
        return s[shortest[0]:shortest[1]] if shortest else ""

def zerosDict(d):
    for v in d.values():
        if v > 0:
            return False
    return True
            
# OUZODYXAZV XYZ {X: 1, Y: 1, Z: 1}
# O UZODYXAZV {X: 1, Y: 1, Z: 1} shortest = ""
# OU ZODYXAZV {X: 1, Y: 1, Z: 1} shortest = ""
# OUZ ODYXAZV {X: 1, Y: 1, Z: 0} shortest = ""
# OUZO DYXAZV {X: 1, Y: 1, Z: 0} shortest = ""
# OUZOD YXAZV {X: 1, Y: 1, Z: 0} shortest = ""
# OUZODY XAZV {X: 1, Y: 0, Z: 0} shortest = ""
# OUZODYX AZV {X: 0, Y: 0, Z: 0} shortest = "OUZODYX"
# O UZODYX AZV {X: 0, Y: 0, Z: 0} shortest = "UZODYX"
# OU ZODYX AZV {X: 0, Y: 0, Z: 0} shortest = "ZODYX"
# OUZ ODYX AZV {X: 0, Y: 0, Z: 1} shortest = "ZODYX"
# OUZ ODYXA ZV {X: 0, Y: 0, Z: 1} shortest = "ZODYX"
# OUZ ODYXAZ V {X: 0, Y: 0, Z: 0} shortest = "ZODYX"
# OUZO DYXAZ V {X: 0, Y: 0, Z: 0} shortest = "DYXAZ"
# OUZOD YXAZ V {X: 0, Y: 0, Z: 0} shortest = "YXAZ"
# OUZODY XAZ V {X: 0, Y: 1, Z: 0} shortest = "YXAZ"
# OUZODY XAZV {X: 0, Y: 1, Z: 0} shortest = "YXAZ"
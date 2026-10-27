class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 2:
            # "" -> 0
            # "a" -> 1
            # "aa" -> 1
            # "ab" -> 2
            return len(set(s))
        

        l = 0
        p = 1

        maxx = 0
        currs = set(s[l])
        while p < len(s):
            if s[p] not in currs:
                currs.add(s[p])
                p += 1
                maxx = max(len(currs), maxx)
            else:
                currs.remove(s[l])
                l += 1
        
        return maxx

# zx yzxyz, l=0, r=1
# zxy zxyz, l=0, r=2
# zxyz xyz, l=0, r=3 duplicates
# z xyz xyz, l=1, r=3
# z xyzx yz, l=1, r=4 duplicates
# zx yzx yz, l=2, r=4
# zx yzxy z, l=2, r=5 duplicates
# zxy zxy z, l=3, r=5
# zxy zxyz, l=3, r=6 duplicates
# zxyz xyz, l=4, r=6

# pwwkew, l=0, r=1 {p, w}
# pww kew, l=0, r=2 {p, w} duplicates
# p ww kew, l=1, r=2 {w} duplicates
# pw w kew, l=2, r=2 {w}
# pw wk ew, l=2, r=3 {w, k}
# pw wke w, l=2, r=4 {w, k, e}
# pw wkew, l=2, r=5 {w, k, e} duplicates
# pww kew, l=3, r=5 {w, k, e}

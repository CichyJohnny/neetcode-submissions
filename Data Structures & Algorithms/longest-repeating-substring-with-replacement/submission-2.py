class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        p = 0

        curr = {}
        maxx = 0
        while p < len(s):
            required = sum(curr.values()) - max(curr.values()) if curr else 0

            if required <= k:
                curr[s[p]] = curr.get(s[p], 0) + 1

                required = sum(curr.values()) - max(curr.values()) if curr else 0
                if required <= k:
                    maxx = max(sum(curr.values()), maxx)
                
                p += 1
            else:
                curr[s[l]] = curr.get(s[l], 0) - 1

                l += 1
        
        return maxx

# XYYX
# X YYX, l=0, p=0, k=2, maxx=1
# XY YX, l=0, p=1, k=1, maxx=2
# XYY X, l=0, p=2, k=0, maxx=3
# XYYX, l=0, p=3, k=0, maxx=4

# AAABABB
# A AABABB, l=0, p=0, k=1, maxx=1
# AA ABABB, l=0, p=1, k=1, maxx=2
# AAA BABB, l=0, p=2, k=1, maxx=3
# AAAB ABB, l=0, p=3, k=0, maxx=4
# AAABA BB, l=0, p=4, k=0, maxx=5
# AAABAB B, l=0, p=5, k=0, maxx=5 duplicates
# A AABAB B, l=1, p=5, k=0, maxx=5 duplicates
# AA ABAB B, l=2, p=5, k=0, maxx=5 duplicates
# AAA BAB B, l=3, p=5, k=0, maxx=5 duplicates
# AAAB AB B, l=4, p=5, k=1, maxx=5
# AAAB ABB, l=4, p=6, k=0, maxx=5
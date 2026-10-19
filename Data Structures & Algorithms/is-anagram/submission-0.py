class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_count_s = {}
        char_count_t = {}

        for ss in s: # O(N)
            if ss in char_count_s:
                char_count_s[ss] += 1
            else:
                char_count_s[ss] = 1
        
        for tt in t: # O(N)
            if tt in char_count_t:
                char_count_t[tt] += 1
            else:
                char_count_t[tt] = 1
        
        if char_count_s.keys() != char_count_t.keys(): # O(k)
            return False
        
        for k, vs in char_count_s.items(): # O(k)
            vt = char_count_t[k]
            if vs != vt:
                return False
        
        return True

        # abc cba {a: 1 b:1 c:1} {a: 1 b:1 c:1} return True
        # abc ab {a: 1 b:1 c:1} {a: 1 b:1} return False at len comparison
        # aaa aaa {a: 3} {a: 3} return True
        # abcc abbc {a: 1 b:1 c:2} {a: 1 b:2 c:1} return False at dict comaprison
        
            
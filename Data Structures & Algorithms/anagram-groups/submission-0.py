class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = {}
        for s in strs:
            tup = self.getTuple(s)
            if tup in results:
                results[tup].append(s)
            else:
                results[tup] = [s]
        
        return [v for v in results.values()]
        
    def getTuple(self, s):
        charcount = [0 for _ in range(26)]
        for ss in s:
            charcount[ord(ss) - 97] += 1
        
        return tuple(charcount)

# [""]
# {""}
# return [[""]]
# ["abc", "cba", "abcc"]
# {[1,1,1,0,...]: ["abc"]}
# {[1,1,1,0,...]: ["abc","cba"]}
# {[1,1,1,0,...]: ["abc","cba"], [1,1,2,0,...]: ["abcc"]}
# return [["abc", "cba"], ["abcc"]]
# ["abb", "aab"]
# {[1,2,0,0,...]: ["abb"]}
# {[1,2,0,0,...]: ["abb"], [2,1,0,0,...]: ["aab"]}
# return [["abb"], ["aab"]]

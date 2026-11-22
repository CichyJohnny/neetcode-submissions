class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = set()
        self.maxLength = 0
        self.cache = {}
        for word in wordDict:
            self.wordDict.add(word)
            self.maxLength = max(self.maxLength, len(word))
        
        return self.search(0, 1)
    
    def search(self, i, j):
        if i in self.cache:
            return self.cache[i]

        ii = i
        jj = j
        results = []
        while jj <= len(self.s) and jj - ii <= self.maxLength:
            if self.s[ii:jj] in self.wordDict:
                result = self.search(jj, jj+1)
                results.append(result)
                self.cache[ii] = result
            jj += 1
        

        if ii == len(self.s):
            return True
        else:
            return any(results)
        
# catsincars
# c
# ca
# cat -> start after cat
# cats s
# catsi si
# catsin sin -> start after sin
# catsinc sinc c
# catsinca sinca ca
# catsincar sincar car -> start after car
# catsincars sincars cars s

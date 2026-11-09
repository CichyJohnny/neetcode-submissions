class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        maxx = 0
        l_longest = -1

        for i in range(len(s)):
            l, p = self.getMaxOdd(i)
            if p - l + 1 > maxx:
                maxx = p - l + 1
                l_longest = l
        
        for i in range(len(s) - 1):
            l, p = self.getMaxEven(i)
            if p - l + 1 > maxx:
                maxx = p - l + 1
                l_longest = l
        
        return s[l:(l + maxx)]
    
    def getMaxOdd(self, i):
        l = i
        p = i
        while 1 <= l and p < len(self.s) - 1 and self.s[l - 1] == self.s[p + 1]:
            l -= 1
            p += 1
        
        return (l, p)
    
    def getMaxEven(self, i):
        l = i
        p = i + 1
        if self.s[l] != self.s[p]:
            return (l, l)

        while 1 <= l and p < len(self.s) - 1 and self.s[l - 1] == self.s[p + 1]:
            l -= 1
            p += 1
        
        return (l, p)

# class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.s = s
        maxx = 0
        l_longest = -1

        for i in range(len(s)):
            l, p = self.getMaxOdd(i)
            if p - l + 1 > maxx:
                maxx = p - l + 1
                l_longest = l
        
        for i in range(len(s) - 1):
            l, p = self.getMaxEven(i)
            if p - l + 1 > maxx:
                maxx = p - l + 1
                l_longest = l
        
        return s[l_longest:(l_longest + maxx)]
    
    def getMaxOdd(self, i):
        l = i
        p = i
        while 1 <= l and p < len(self.s) - 1 and self.s[l - 1] == self.s[p + 1]:
            l -= 1
            p += 1
        
        return (l, p)
    
    def getMaxEven(self, i):
        l = i
        p = i + 1
        if self.s[l] != self.s[p]:
            return (l, l)

        while 1 <= l and p < len(self.s) - 1 and self.s[l - 1] == self.s[p + 1]:
            l -= 1
            p += 1
        
        return (l, p)

# ababd
# a, l=0, p=0, return (0, 0)
# b, l=1, p=1
# aba, l=0, p=2, return (0, 2)
# a, l=2, p=2
# bab, l=1, p=3, return (1, 3)
# b, l=4, p=4, return (4, 4)
# d, l=5, p=5, return (5, 5)

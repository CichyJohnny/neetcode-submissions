class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_to_close = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        for ss in s:
            if ss in open_to_close.keys():
                stack.append(ss)
            else:
                if stack and open_to_close[stack[-1]] == ss:
                    stack.pop(-1)
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False

# ([{}])
# ( stack=["("]
# [ stack=["(", "["]
# { stack=["(", "[", "{"]
# } stack=["(", "["
# ] stack=["(", "["]
# ) stack=[]
# True

# [(])
# [ stack=["["]
# ( stack=["[", "("]
# ( -> ) != ]
# False
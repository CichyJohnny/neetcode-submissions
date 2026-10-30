class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if self.isNumber(tokens[i]):
                stack.append(int(tokens[i]))
                pass
            else:
                result = 0
                if tokens[i] == "+":
                    num1, num2 = stack.pop(-1), stack.pop(-1)
                    result = num2 + num1
                elif tokens[i] == "-":
                    num1, num2 = stack.pop(-1), stack.pop(-1)
                    result = num2 - num1
                elif tokens[i] == "*":
                    num1, num2 = stack.pop(-1), stack.pop(-1)
                    result = num2 * num1
                elif tokens[i] == "/":
                    num1, num2 = stack.pop(-1), stack.pop(-1)
                    result = int(num2 / num1)
                stack.append(result)
        
        return stack[0]

    def isNumber(self, num):
        try:
            int(num)
            return True
        except:
            return False

# ["4","13","5","/","+"]
# [4]
# [4, 13]
# [4, 13, 5]
# [4] num1=5 num2=13 13//5=2 -> [4, 2]
# [] num1=2 num2=4 4+2=6 -> [6]
# return 6

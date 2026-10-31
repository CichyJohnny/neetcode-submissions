class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0 for _ in range(len(temperatures))]

        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                top = stack.pop()
                results[top] = i - top
            
            stack.append(i)
        
        return results

# [30,38,30,36,35,40,28]
# 30, empty stack=[0], results=[0,0,0,0,0,0,0]
# 38, 38>30 stack=[1], results=[1-0,0,0,0,0,0,0]
# 30, 30<38 stack=[1,2], results=[1,0,0,0,0,0,0]
# 36, 36>30 stack=[1,3], results=[1,0,3-2,0,0,0,0]
# 35, 35<36 stack=[1,3,4], results=[1,0,1,0,0,0,0]
# 40, 40>35, 40>36, 40>38 stack=[5], results=[1,5-1,1,5-3,5-4,0,0]
# 28, 28<40 stack=[5,6], results=[1,4,1,2,1,0,0]

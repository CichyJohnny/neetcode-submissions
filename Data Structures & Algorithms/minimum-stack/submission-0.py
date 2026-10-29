class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_min.append(min(val, self.stack_min[-1] if self.stack_min else float("inf")))
        

    def pop(self) -> None:
        self.stack.pop()
        self.stack_min.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack_min[-1]
        
# push(5) stack=[5], stack_min=[5]
# push(3) stack=[5, 3], stack_min=[5, 3]
# push(4) stack=[5, 3, 4], stack_min=[5, 3, 3]
# getMin() -> 3
# pop() stack=[5, 3], stack_min=[5, 3]
# pop() stack=[5], stack_min=[5]
# getMin() -> 5

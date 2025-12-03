class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []   # stores current minimums

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If minStack is empty or val <= current min, push to minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # If popped value was the minimum, pop from minStack too
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

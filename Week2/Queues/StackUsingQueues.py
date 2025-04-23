class MyStack:
    def __init__(self):
        self.stack = []
        self.tops = -1

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.tops += 1
        return

    def pop(self) -> int:
        self.tops -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[self.tops]

    def empty(self) -> bool:
        return self.tops < 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

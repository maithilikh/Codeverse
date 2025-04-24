class MyQueue:

    def __init__(self):
        self.normSt = []
        # self.tempSt = []

    def push(self, x: int) -> None:
        self.normSt.append(x)

    def pop(self) -> int:
        # move all elements to temporary stack, remove from front and push back all elements to original stack
        frntElem = self.normSt[0]
        self.normSt = self.normSt[1:]
        return frntElem

    def peek(self) -> int:
        # move n-1 elements into temporary stack and see topmost element of original stack
        return self.normSt[0]

    def empty(self) -> bool:
        return len(self.normSt) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

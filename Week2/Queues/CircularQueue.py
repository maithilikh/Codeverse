class MyCircularQueue:

    def __init__(self, k: int):
        self.cirQ = [-1 for i in range(k)]
        self.fr = -1
        self.rr = -1
        self.k = k

    def isEmpty(self) -> bool:
        return max(self.cirQ) == -1

    def isFull(self) -> bool:
        return self.cirQ[(self.fr-1)%(self.k)] != -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            if self.fr == -1 and self.rr == -1:
                self.fr += 1
            self.rr = (self.rr+1)%(self.k)
            self.cirQ[self.rr] = value
            return True

    def deQueue(self) -> bool:        
        if self.isEmpty():
            return False
        else:
            self.cirQ[self.fr] = -1
            self.fr = (self.fr+1)%(self.k)
            return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.cirQ[self.fr]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.cirQ[self.rr]


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

class MyCircularQueue:

    def __init__(self, k: int):
        self.cirQ = [-1 for i in range(k)]
        self.fr = -1
        self.rr = -1
        self.k = k

    def enQueue(self, value: int) -> bool:
        # self.fr = (self.fr +1)%self.k
        # if not ((self.rr == self.fr + self.k) or (self.rr == self.fr)):
        #     self.cirQ[self.fr] = value
        #     return True
        # else:
        #     return False

    def deQueue(self) -> bool:        
        # if self.rr <= self.fr:
        #     self.rr = (self.fr -1)%self.k
        #     return True
        # else:
        #     return False

    def Front(self) -> int:
        return self.cirQ[(self.fr)%(self.k)]

    def Rear(self) -> int:
        return self.cirQ[(self.rr)%(self.k)]

    def isEmpty(self) -> bool:
        return self.rr > self.fr

    def isFull(self) -> bool:
        return (self.rr == self.fr + self.k) or (self.rr == self.fr)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

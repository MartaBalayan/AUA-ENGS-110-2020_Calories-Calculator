class DequeArray:
    def __init__(self,size):
        self.deque = []
        for i in range(size):
            self.deque.append(None)

    def addFirst(self,NewValue):
        if self.deque[0] is None:
            self.deque[0]=NewValue
        elif self.deque[-1] is None:
            a = 1%len(self.deque)
            self.deque = self.deque[-a:]+self.deque[:-a]
            self.deque[0] = NewValue
        else:
            self.resize()
            a = 1 % len(self.deque)
            self.deque = self.deque[-a:] + self.deque[:-a]
            self.deque[0] = NewValue

    def addLast(self,NewValue):
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                self.deque[i]=NewValue
                return
        self.resize()
        last_index=int(len(self.deque)/2)
        self.deque[last_index]=NewValue

    def removeFirst(self):
        self.deque.pop(0)
        self.deque.append(None)

    def removeLast(self):
        last_index = self.last_index()
        self.deque[last_index]=None

    def first(self):
        return self.deque[0]

    def last(self):
        l_index = self.last_index()
        return self.deque[l_index]

    def last_index(self):
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                return i-1
        return len(self.deque)-1

    def resize(self):
        b = []
        for i in range(len(self.deque)):
            b.append(None)
        self.deque = self.deque + b

    def print_deque(self):
        print (self.deque)
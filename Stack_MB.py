class Stack:
    def __init__(self):
        self.Stack = []

    def AddElement(self,DataValue):
        if DataValue not in self.Stack:
            self.Stack.append(DataValue)
            return True
        else:
            return False

    def RemoveElement(self):
        if len(self.Stack) <= 0:
            return "Stack is empty"
        else:
            return self.Stack.pop()

    def TopElement(self):
        return self.Stack[-1]

    def StackIsEmpty(self):
        if len(self.Stack) == 0:
            return True
        else:
            return False

    def StackSize(self):
        return len(self.Stack)

    def PrintStack(self):
        for i in range(len(self.Stack)):
            print(self.Stack[i])
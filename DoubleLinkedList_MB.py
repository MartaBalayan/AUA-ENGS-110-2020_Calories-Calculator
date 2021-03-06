class Node:
    def __init__(self,DataValue=None):
        self.DataValue = DataValue
        self.NextValue = None
        self.PrevValue = None

class DoubleLinkedList:
    last = None

    def __init__(self):
        self.HeadValue= None

    def listprint(self):
        node = self.HeadValue
        while node is not None:
            print(node.DataValue),
            node = node.NextValue

    def addFirstElement(self,NewData):
        NewNode = Node(NewData)
        NewNode.NextValue = self.HeadValue
        if self.HeadValue is None:
            self.last = NewNode
        if self.HeadValue is not None:
            self.HeadValue.PrevValue = NewNode
        self.HeadValue = NewNode

    def addLast(self, NewData):
        NewNode = Node(NewData)
        NewNode.NextValue = None
        if self.HeadValue is None:
            NewNode.PrevValue = None
            self.HeadValue = NewNode
            return
        last = self.HeadValue
        while (last.NextValue is not None):
            last = last.NextValue
        last.NextValue = NewNode
        NewNode.PrevValue = last
        self.last = NewNode
        return

    def InsertAfter(self, PrevNode, NewData):
        if PrevNode is None:
            return
        NewNode = Node(NewData)
        NewNode.NextValue = PrevNode.NextValue
        PrevNode.NextValue = NewNode
        NewNode.PrevValue = PrevNode
        if NewNode.NextValue is not None:
            NewNode.NextValue.PrevValue = NewNode

    def InsertBefore(self, NextNode, NewData):
        if NextNode is None:
            return
        NewNode = Node(NewData)
        NewNode.PrevValue = NextNode.PrevValue
        NextNode.PrevValue = NewNode
        NewNode.NextValue = NextNode
        if NewNode.NextValue is not None:
            NewNode.PrevValue.NextValue = NewNode

    def RemoveNode(self, RemoveKey):
        HeadValue = self.HeadValue

        if HeadValue is not None:
            if HeadValue.DataValue == RemoveKey:
                self.HeadValue = HeadValue.NextValue
                HeadValue = None
                return
        while HeadValue is not None:
            if HeadValue.DataValue == RemoveKey:
                break
            prev = HeadValue
            HeadValue = HeadValue.NextValue
        if HeadValue == None:
            return
        prev.NextValue = HeadValue.NextValue

        self.HeadValue = None

    def RemoveFirstElement(self):
        self.RemoveNode(self.First())

    def RemoveLastElement(self):
        self.RemoveNode(self.last.DataValue)
        self.last = self.last.PrevValue

    def First(self):
        return self.HeadValue.DataValue

    def Last(self):
        return self.last.DataValue

    def IndexOf(self,node):
        element = self.HeadValue
        index = 0
        while element is not None:
            if element.DataValue == node:
                return index
            element = element.NextValue
            index += 1

    def Size(self):
        size = 1
        element = self.HeadValue
        if element == None:
            return 0
        while element is not None:
            if element.NextValue == None:
                return size
            element = element.NextValue
            size += 1
class Node:
    def __init__(self,DataValue=None):
        self.DataValue = DataValue
        self.NextValue = None

class SLinkedList:
    def __init__(self):
        self.HeadValue = None

    def ListPrint(self):
        PrintValue = self.HeadVal
        while PrintValue is not None:
            print(PrintValue.DataValue)
            PrintValue = PrintValue.NextValue

    def FirstElement(self):
        return self.HeadValue.DataValue

    def LastElement(self):
        last = self.HeadValue
        while last is not None:
            if last.NextValue == None:
                return (last.DataValue)
            last = last.NextValue

    def Beginning(self,NewData):
        NewNode = Node(NewData)
        NewNode.NextValue = self.HeadValue
        self.HeadValue = NewNode

    def End(self,NewData):
        NewNode = Node(NewData)
        if self.HeadValue is None:
            self.HeadValue = NewNode
            return
        LastElement = self.HeadValue
        while(LastElement.NextValue is not None):
            LastElement = LastElement.NextValue
        LastElement.NextValue=NewNode

    def InsertAfter(self,middle_node,NewData):
        if middle_node is None:
            print("Error. That node is absent")
            return
        NewNode = Node(NewData)
        NewNode.NextValue = middle_node.NextValue
        middle_node.NextValue = NewNode

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

        HeadValue = None

    def RemoveFirst(self):
        self.RemoveNode(self.FirstElement())

    def RemoveLast(self):
        self.RemoveNode(self.LastElement())

    def IndexOf(self,node):
        elem = self.HeadValue
        index = 0
        while elem is not None:
            if elem.DataValue == node:
                return index
            elem = elem.NextValue
            index += 1

    def Size(self):
        size = 1
        elem = self.HeadValue
        if elem == None:
            return 0
        while elem is not None:
            if elem.NextValue == None:
                return size
            elem = elem.NextValue
            size += 1
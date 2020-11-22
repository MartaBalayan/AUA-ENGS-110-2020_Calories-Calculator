class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet():
    def __init__(self, capacity):
        self._hashtable = [None] * capacity
        self._capacity = capacity
        self._size = 0

    def hash(self, element):
        return hash(element) % self._capacity

    def hash_str(self, element):
        hash = (ord(element[0])+ord(element[-1]))/2
        return int(hash)%5

    def add(self, element):
        if isinstance(element,str) is True:
            index = self.hash_str(element)
        else:
            index = self.hash(element)
        print(index)
        if (self._hashtable[index] == None):
            self._hashtable[index] = Node(element)
        else:
            n = Node(element, self._hashtable[index])
            self._hashtable[index] = n
        self._size += 1

    def contain(self, element):
        index = self.hash(element)
        n = self._hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        index = self.hash(element)
        n = self._hashtable[index]
        p = None
        while (n != None):
            if (n.data == element):
                if (p == None):
                    self._hashtable[index] = n.next
                else:
                    p.next = n.next
                n.next = None
                self._size -= 1
                return n
            p = n
            n = n.next
        return None

    def size(self):
        return self._size

    def intersection(self, s):
        newSet = HashSet(5)
        for e in self._hashtable:
            while (e != None):
                if (s.contains(e.data)):
                    newSet.add(e.data)
                e = e.next
        return newSet

    def intersectionUpdate(self, s):
        for e in self._hashtable:
            p = None
            while (e != None):
                r = None
                if (not s.contains(e.data)):
                    r = e
                if (r != None):
                    if (p == None):
                        self._hashtable[self.hash(r.data)] = e.next
                    else:
                        p.next = e.next
                    e = e.next
                    self._size -= 1
                else:
                    p = e
                    e = e.next

    def print(self):
        print("printing hashset elements")
        for e in self._hashtable:
            while (e != None):
                print(e.data)
                e = e.next

    def __iter__(self):
        for e in self._hashtable:
            if (e != None):
                self._elem = e;
                break
        return self

    def __next__(self):
        if self._elem == None:
            raise StopIteration

        tmp = self._elem
        if (self._elem.next != None):
            self._elem = self._elem.next
        else:
            index = self.hash(self._elem.data)
            self._elem = None
            for i in range(index + 1, len(self._hashtable)):
                if (self._hashtable[i] != None):
                    self._elem = self._hashtable[i]
                    break
        return tmp.data

def sort_first(HashSet):
    temp_HS=HashSet
    for i in range(len(temp_HS._hashtable)):
        if temp_HS._hashtable[i] != None:
            print(temp_HS._hashtable[i].data)
            temp_HS._hashtable[i]=temp_HS._hashtable[i].next
    for i in range(len(temp_HS._hashtable)):
        if temp_HS._hashtable[i] != None:
            sort_first(temp_HS)
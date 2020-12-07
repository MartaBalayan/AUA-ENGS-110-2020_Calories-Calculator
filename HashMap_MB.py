class Entry():
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashMap():
    def __init__(self):
        self._capacity = 26
        self._hashtable = [None] * self._capacity
        self._size = 0

    def _hash(self, element):
        #return element
        return ord(element[0]) % self._capacity

    def put(self, key, value):
        index = self._hash(key)
        #for i in range(index, len(self._hashtable)):
        if (self._hashtable[index] != None):
            for i in range(len(self._hashtable[index])):
                if key == self._hashtable[index][i].name:
                    oldValue = self._hashtable[index].value
                    self._hashtable[index].value = value
                    #return oldValue
                    self._size += 1
                    break
                else:
                    try:
                        self._hashtable[index].append(value)
                    except Exception as e:
                        self._hashtable_new = []
                        self._hashtable_new.append(self._hashtable)
                        self._hashtable_new.append(value)
                        self._hashtable = self._hashtable_new
                    self._size += 1
                    break
                    # temp_value = self._hashtable[index]
                    # self._hashtable = []
                    # self._hashtable.append(temp_value)
                    # self._hashtable.append(value)
        else:
            self._hashtable[index] = []
            self._hashtable[index].append(value)
            #self._hashtable[index] = Entry(key, value)
            self._size += 1
            return None

    def get(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                for j in range(len(self._hashtable[index])):
                    if key == self._hashtable[i][j].name:
                        return self._hashtable[i][j].value
            else:
                return None

    def hasKey(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                for j in range(len(self._hashtable[index])):
                    if key == self._hashtable[i][j].name:
                        print(key, "is present in the hashmap")
                        return True
                        break
            else:
                print(key, "is not present in the hashmap")
                return False

    def remove(self, key):
        index = self._hash(key)
        for i in range(index, len(self._hashtable)):
            if (self._hashtable[i] != None):
                for j in range(len(self._hashtable[index])):
                    if key == self._hashtable[i][j].name:
                        print("Removed ",self._hashtable[i][j].value,"from HasMap")
                        self._hashtable[i] = None
                        break
            else:
                print ("Such entry was not found")
                return None

    def size(self):
        return self._size

    def print(self):
        #print("printing hashset elements")
        for elem in self._hashtable:
            if elem != None:
                for i in range(len(elem)):
                    print(elem[i].value)

    def __iter__(self):
        for i in range(len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break
        return self

    def __next__(self):
        if self._index >= len(self._hashtable):
            raise StopIteration
        tmpInd = self._index
        self._index = len(self._hashtable)
        for i in range(tmpInd + 1, len(self._hashtable)):
            if (self._hashtable[i] != None):
                self._index = i;
                break

        return self._hashtable[tmpInd].value
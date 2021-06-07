class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def add(self,e):
        newest = _Node(e, None)

        if self.isEmpty():
            self._head = newest
        else:
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def search(self,key):
        p = self._head
        index = 0

        while p:
            if p._element == key:
                return index
            p = p._next
            index += 1

        return -1
    def addanywhere(self,e,position):
        newest = _Node(e, None)
        p = self._head
        i = 1

        while i < position - 1:
            p = p._next
            i = i + 1

        p._next = newest
        newest._next = p._next

        self._size += 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end='  ')
            p = p._next
        print()


item = LinkedList()
item.add(5)
item.add(4)
item.add(7)
item.add(2)

item.display()
l = item.search(7)
a = item.search(88)
print("item is in index ", l)
print(a)
item.isEmpty()
print("*" * 10)
item.addanywhere(22,2)
item.display()
"""

Author: Aayush Shahi Thakuri

"""
class MinStack:
    def __init__(self):
        self._items = []            # Just use a list internally
        self._min=[]

    def empty(self):
        return len(self._items) == 0

    def min(self):
        if(self.empty()):
            raise IndexError('pop(): empty stack')
        return self._min[-1]

    def push(self, x):
        if self.empty():
            self._min.append(x)

        else:
           self._min.append(min([x,self.peek()]))

        self._items.append(x)

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        self._min.pop()
        return self._items.pop()

    def peek(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._items[-1]
class Stack:
    def __init__(self): 
        self.stack = []
    def push(self, value): 
        self.stack.append(value)
    def pop(self): 
        if self.is_empty():
            raise IndexError("Pop from empty stack")    
        return self.stack.pop()
    def __len__(self): 
        return len(self.stack)
    def is_empty(self): 
        return self.__len__() == 0
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]


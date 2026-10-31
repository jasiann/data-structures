class DynamicArray:
    def __init__(self, capacity=1): 
        self.capacity = capacity
        self.size = 0
        self.block = [None] * capacity
        
    def __len__(self):
        return self.size

    def __getitem__(self, index): 
        if not (0 <= index < self.size):
            raise IndexError("index out of range")
        return self.block[index]
    def append(self, value):
        if self.capacity == self.size:
            self._resize(2 * self.capacity) 
            
        self.block[self.size] = value
        self.size += 1
    def _resize(self, new_capacity): 
        new_block = [None] * new_capacity
        for i in range(self.size): 
            new_block[i] = self.block[i]
            
        self.block = new_block
        self.capacity = new_capacity
        
    def __setitem__(self, index, value):
        if not(0 <= index < self.size): 
            raise IndexError("index out of range")
        self.block[index] = value
        
    def pop(self): 
        if self.size == 0: 
            raise IndexError("pop from empty array")
        value = self.block[self.size - 1]
        self.block[self.size - 1] = None
        self.size -= 1
        return value
        

            
        
        
    

        
            
    
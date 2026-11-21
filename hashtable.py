class HashMap:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return value
        bucket.append((key, value))
        self.size += 1
        if self.size / self.capacity > 0.75:
            self._resize(self.capacity * 2)
        return value

    def get(self, key):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key not found")

    def delete(self, key):
        bucket = self.buckets[self._index(key)]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError("Key not found")

    def __len__(self):
        return self.size

    def __contains__(self, key):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def _resize(self, new_capacity):
        old_buckets = self.buckets
        self.capacity = new_capacity
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
            
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
    
    
    
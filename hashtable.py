class HashMap: 
    def __init__(self, capacity = 8): 
        self.capacity = capacity
        self.size = 0 
        self.buckets = [[] for _ in range(capacity)] #this one works becuase for range it creates an unique instance for [] 
        
    def _index(self, key):
        return hash(key) % self.capacity 
    
    def put(self, key, value): 
        bucket = self.buckets[self._index(key)]
        for i, (k,v) in enumerate(bucket): 
            if k == key: 
                bucket[i] = (key,value)
                return value 
        bucket.append((key,value)) #If the key wasn't found in the loop, append it as a new pair
        self.size += 1
        return value
                
    def get(self,key): 
        bucket = self.buckets[self._index(key)]  #Use  _index method so it works on non-integers (like strings)
        
        for k, v in bucket: 
            if k == key: 
                return v 
        raise KeyError("Key not found")
    
    def delete(self, key): 
        bucket = self.buckets[self._index(key)]
        for i, (k,v) in enumerate(bucket):
            if k == key: 
                del bucket[i]
                self.size -= 1
                return
        raise KeyError("Key not found")
    
    def __len__(self): 
        return self.size 
    
    def __contains__(self,key):
        bucket = self.buckets[self._index(key)]
        for k, v in bucket: 
            if k == key: 
                return True
        return False
    
    
        
                
            
        
        
        
        
    
    
        
        
        
        
        
        
    
    
        
    
    
    

'''
https://www.youtube.com/watch?v=7ABFKPK2hD4
'''
class Node: 
    def __init__(self, key, val): 
        self.key, self.val = key, val 
        self.prev = self.next = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        # left = LRU, right = most recently used 
        self.left, self.right= Node(0, 0), Node(0, 0) #let them point to dummy nodes first 
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node): # remove node from list 
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node): # insert node at right 
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
    
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key]) # remove node from the list
            self.insert(self.cache[key]) # insert it to the right since it's most recently used 
            return self.cache[key].val 
        return -1 # node does not exist in list

    def put(self, key, value): 
        if key in self.cache: # key already exists in cache
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

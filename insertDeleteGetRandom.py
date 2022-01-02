
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = list()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.data: 
            self.data.append(val)
            return True 
        return False 
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data: 
            return False
        
        self.data.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if len(self.data) < 1: 
            return False 
        rand_idx = random.choice([_ for _ in range(len(self.data))])
        return self.data[rand_idx]

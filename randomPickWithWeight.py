
'''
Return index of the value in w that pickIndex generates with value / sum(w) probability. 

Idea: Prefix sum + binary search
Given w = [10, 7, 8, 10]
1. create an array prefixSums = [10, 17, 25, 35]
2. in pickIndex, generate a random number between 1 and 35
    a. using binary search, look for the index of random number in prefixSums
    (going to pick index corresponding to the upper bound of the random number)
    and that index is going to map to index in w
    
Time Complexity: O(N)
'''
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefixSums.append(prefix_sum)
        self.total_sum = prefix_sum
        
    def pickIndex(self) -> int:
        import random 
        target = random.randint(1, self.total_sum) 
        
        left, right = 0, len(self.prefixSums)-1
        ans = None
        while left <= right: #classic binary search 
            mid = (left+right)//2
            if target <= self.prefixSums[mid]:
                ans = mid
                right = mid-1
            else: 
                left = mid +1
        return ans 


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

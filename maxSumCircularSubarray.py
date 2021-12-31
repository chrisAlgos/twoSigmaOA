
'''
idea: to get the maximum subarray sum, there could be 2 cases: 

1. max subarray sum is found within start and end of the given array 
    - use usual Kadane's algo to get max sum 
2. max subarray sum crosses bounds of the given array (subarray that gives max sum circles around)
    - this means that the minimum subarray sum will exist between start and end of the given array
    - minimum subarray sum = total sum - maximum subarray sum ==> max subarray sum = total sum - min subarray sum 
    - Hence find min subarray sum 
    
Using this approach, find minimum subarray sum (2nd case) AND max subarray sum (1st case)

What if the entire array is negative? regular Kadane's algo finds the negative number so just return option 1's finalMaxSum when this is the case.


'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        runMaxSum, runMinSum, finalMaxSum, finalMinSum = -float('inf'), float('inf'), -float('inf'), float('inf')
        allNegatives = True
        
        for num in nums: 
            
            # if there is a positive number, set allNegatives to False 
            if num >= 0: 
                allNegatives = False 
                
            # get runMinSum and runMaxSum
            runMaxSum, runMinSum = max(runMaxSum+num, num), min(runMinSum + num, num)
            
            # set finalMaxSum, finalMinSum
            finalMaxSum, finalMinSum = max(finalMaxSum, runMaxSum), min(finalMinSum, runMinSum)
            
        return finalMaxSum if allNegatives else max(finalMaxSum, sum(nums)-finalMinSum)

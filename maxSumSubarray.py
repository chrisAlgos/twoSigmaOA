'''
Find the maximum subarray sum 

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Time | Space = O(N) | O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, runSum = -float('inf'), 0 
        for num in nums: 
            # if num is negative then we want to restart running sum 
            if runSum < 0: 
                runSum = 0 
            runSum += num
            maxSum = max(maxSum, runSum)
        return maxSum 
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxResult, maxRunSum = -float('inf'), -float('inf')
        
        for num in nums: 
            maxRunSum = max(maxRunSum+num, num) # at each pass, see which one is greater: maxRunSum up until i plus num or num?
            maxResult = max(maxResult, maxRunSum) # at each pass, update maxResult
        return maxResult

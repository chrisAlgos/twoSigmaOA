'''
Find the maximum subarray sum 

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.


Time | Space = O(N) | O(1)
'''
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

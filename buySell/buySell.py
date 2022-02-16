'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Maximize profit by choosing one day to buy stock and another day to sell stock. 
If you cannot make profit, return 0. 
prices = [7,1,5,3,6,4]
--> buy low, sell high 
Buy at 1, sell at 6 --> max profit = 5 
Technique: Sliding Window 
L, R point to buy and sell prices respectively 
Want: sell > buy to maximize profit 
1. Start R (sell) at index = 1. 
2. If prices[L] (buy price) > prices[R] (sell price) --> reset buy index to sell index 
3. Calculate profit and update max profit 
Time | Space: O(N) | O(1) 
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # want to buy low, sell high 
        L, maxProfit = 0, 0 
        for R in range(1, len(prices)): 
            buy, sell = prices[L], prices[R]
            if sell > buy: # buy > sell 
                L=R 
            profit = prices[R] - prices[L]
            maxProfit = max(maxProfit, profit)
        return maxProfit

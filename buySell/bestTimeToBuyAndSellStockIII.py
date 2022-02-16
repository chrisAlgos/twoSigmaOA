'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        firstBuyFirstSellProfit, secondBuySecondSellProfit = 0, 0 
        firstBuy, secondBuy = float('inf'), float('inf')
        
        for i in range(len(prices)): 
            price = prices[i]
            firstBuy = min(firstBuy, price)
            firstBuyFirstSellProfit = max(firstBuyFirstSellProfit, price-firstBuy)
            #firstBuyFirstSellProfit is used to lower the cost of secondBuy
            secondBuy = min(secondBuy, price - firstBuyFirstSellProfit)
            secondBuySecondSellProfit = max(secondBuySecondSellProfit, price-secondBuy)
        return secondBuySecondSellProfit

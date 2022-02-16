class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        sliding window technique 
        
        ** can only hold at most one share of the stock at any time **
        --> we can get maxProfit by adding consecutive increasing portions 
        
        Valid window: when sell (prices[r]) is greater than buy (prices[l])
        Since we want to add consecutive increasing portions, want to look at profit in each consecutive time slots 
            Thus, if window == valid and right after we add current profit to the maxProfit
            move left to where right currently is so that we can consider profit in the next time snapshot
        '''
        
        l = 0
        maxProfit = 0 
        
        for r in range(1, len(prices)): 
            # if sell > buy --> valid window 
            if prices[r] >= prices[l]: 
                profit = prices[r]-prices[l]
                maxProfit += profit 
                l += 1
            else: # if sell < buy <-- not valid window 
                while prices[l] > prices[r] and l <= r: 
                    l += 1
        return maxProfit 

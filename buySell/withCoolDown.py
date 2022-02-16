class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        
        dp memoization: 
        
        "may complete as many transactions as you like": create a decision tree 
        
        3 different states: 
            1. buy state 
            2. cooldown state (not doing anything)
            3. sell state 
            
        ** When we start out (idx = 0 in prices), we are always at the buy state. 
        
        Buy at current idx in prices: 2 choices 
            1. Sell in next state
            2. Cooldown in next state
            
        Sell at current idx in prices: 2 choices 
            1. Buy in next state 
            2. Cooldown in next state 
            
        cache results from bottom up...key = (current index, buying boolean), val = max_profit
        '''
        # State: Buying / Selling 
        # If Buy: i+1
        # If Sell: i+2 (+2 due to cooldown)
        # True for buy next time, False for sell next time 
        
        dp = {} # hash set 
        
        def dfs(idx, buying): 
            
            #### backtrack / base cases ######
            
            # if we go out of bounds, we don't make any profit 
            if idx >= len(prices): 
                return 0 
            
            # if key already in cache, then return corresponding max profit 
            if (idx, buying) in dp: 
                return dp[(idx, buying)]
            
            
            #### what to do at current state #####
            if buying: # boolean that indicates what we have to do at current state
                # 2 things we can do rn: buy or coolDown (don't do anything)
                buy = dfs(idx+1, False) - prices[idx] # subtract current price from max profit cuz we just bought
                coolDown = dfs(idx+1, True) # didn't do anything rn, so we still need to buy
                dp[(idx, buying)] = max(buy, coolDown)
            else: # sell state 
                # 2 things we can do rn: sell or coolDown (don't do anything) 
                sell = dfs(idx+2, True) + prices[idx] # add cuz we make money from selling, add 2 to idx --> automatically cool down after selling 
                coolDown = dfs(idx+1, False) # didn't do anythign rn, so we still need to sell 
                dp[(idx, buying)] = max(sell, coolDown)
            
            return dp[(idx, buying)]
        
        return dfs(0, True)

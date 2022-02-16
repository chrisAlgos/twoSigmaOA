def maxProfitWithKTransactions(prices, k):
	
	if k == 0: return 0 
	if len(prices) == 0: return 0 
	
	# 1. create a matrix and instantiate values to 0 
	# d stands for price at day d, t stands transaction 
	profits = [[0 for d in range(len(prices))] for t in range(k+1)] 
	
	### Remember: 1 transaction = buy + sell
	# want to fill max profit for (t)th transaction for range in prices: up to & including (d)th day: profits[t][d]
	for t in range(1, k+1): 
		maxProfitWhenYouBuy= float('-inf')
		for d in range(1, len(prices)): 
			# get max profit at the time of buy for the t'th transaction (buy only, no sell yet): 
			# subtract 'buy' prices[d-1] for the t'th transaction from previous transaction max profit
			# max profit at the time of buy for the t'th transaction = profits[t-1][d-1]
			# = previous transaction max profit at the time of buy 
			# = profits[t-1][d-1]
			maxProfitWhenYouBuy = max(maxProfitWhenYouBuy, profits[t-1][d-1]-prices[d-1])
			sell, noSell = maxProfitWhenYouBuy + prices[d], profits[t][d-1]
			profits[t][d] = max(sell, noSell)
	
	return profits[-1][-1]

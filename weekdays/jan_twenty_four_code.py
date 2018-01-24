def get_max_profit_non_neg(stock_prices):
	#Want to buy low and sell high

	if len(stock_prices)<2:
		return "Not enough prices to calculate profit"
	else:
		profit_list = []
		i=0
		for value in range(len(stock_prices)-1):
			if stock_prices[i] > stock_prices[i+1]:
				i=i+1
				continue
			else:
				buy_price = stock_prices[i]
				sell_price = max(stock_prices[i+1:])
				#print(buy_price, sell_price)
				profit_list.append(sell_price-buy_price)
				i=i+1
		if not profit_list:
			return "Can't make a profit"
		else:
			#print(profit_list)
			return max(profit_list)      # Returns an integer representing the max profit from stock sales

def get_max_profit(stock_prices):
	#Want to buy low and sell high
	if len(stock_prices)<2:
		return "Not enough prices to calculate profit"
	else:
		profit_list = []
		i=0
		for value in range(len(stock_prices)-1):
			buy_price = stock_prices[i]
			sell_price = max(stock_prices[i+1:])
			#print(buy_price, sell_price)
			profit_list.append(sell_price-buy_price)
			i=i+1

	return max(profit_list)      # Returns an integer representing the max profit from stock sales



### Test Cases

#stock_prices = [0,1,2,3,4,5,6,7,8,9,10]
#stock_prices = [10,9,8,7,6,5,4,3,2,1,0]
#stock_prices = [2,7,5,3,7,9,10,5,7,9,10]
#stock_prices = [0,0,0,0,0,0,0,0,0,0,0,0]
stock_prices = [2]



max_profit = get_max_profit(stock_prices)
print(max_profit)
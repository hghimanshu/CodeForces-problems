def predictStocks(arr):
    min_price, max_profit = float('inf'), 0.0
    for i in arr:
        max_profit_sell_today = i - min_price
        max_profit = max(max_profit, max_profit_sell_today)
        min_price = min(min_price, i)
    
    return max_profit


arr = [310,315,275,295,260,270,290,230,255,250]
# arr = [7,1,5,3,6,4]
print(predictStocks(arr))
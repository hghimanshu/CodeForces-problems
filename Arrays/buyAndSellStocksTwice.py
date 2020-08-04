def buy_and_sell_stock_twice(arr):
    max_profit, min_price = 0, float('inf')
    first_buy_sell_price = [0]* len(arr)

    for id, i in enumerate(arr):
        min_price = min(i, min_price)
        max_profit = max(max_profit, i - min_price)
        first_buy_sell_price[id] = max_profit
    
    max_price = float('-inf')
    for i, price in reversed(list(enumerate(arr[1:], 1))):
        max_price = max(max_price, price)
        max_profit = max(max_profit, max_price - price + first_buy_sell_price[i-1])
    return max_profit


arr = [12,11,13,9,12,8,14,13,15]
print(buy_and_sell_stock_twice(arr))
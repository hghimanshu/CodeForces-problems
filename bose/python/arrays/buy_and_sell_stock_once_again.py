
def get_max_profit(arr):
    # min_price =0
    # max_profit =0


    min_price = arr[0]
    profit = 0
    for price in arr:
        if price < min_price:
            min_price = price
        profit = max(price - min_price,profit)

    print(profit)


if __name__ == "__main__":
    stock_prices = [310,315,275,295,260,270,290,230,255,250]
    get_max_profit(stock_prices)
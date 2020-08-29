def getMax(a,b):
    return max(a,b)

def getMin(a,b):
    return min(a,b)

def buyAndSellTwice(a,n):
    buy1=100000
    buy2=100000
    profit1 = 0
    profit2 = 0

    for i in range(0,n):
        buy1 = getMin(buy1,a[i])
        profit1 = getMax(profit1,a[i]-buy1)

        buy2 = getMin(buy2,a[i]-profit1)
        profit2= getMax(profit2,a[i]-buy2)

        print("Index %d : Buy1 is %d , Profit1 is %d , Buy2 is %d , Profit2 is %d"%(i,buy1,profit1,buy2,profit2))

    return profit2

if __name__ == "__main__":
    # arr = [3, 3, 5, 0, 0, 3, 1, 4]
    arr = [ 2, 30, 15, 10, 8, 25, 80]
    print(buyAndSellTwice(arr,len(arr)))






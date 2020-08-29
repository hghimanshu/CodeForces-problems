import time

def getMax(a,b):
    return max(a,b)

def getMin(a,b):
    return min(a,b)

def getMaximumProfit(a,n):
    if a is None:
        return 0
    elif n==1:
        return 0
    
    buy_array=[0]*n
    sell_array=[0]*n

    min_buy_seen = 0
    for i in range(0,n):
        if i==0:
            buy_array[0]=a[i]
            min_buy_seen=a[i]
        else:
            min_buy_seen=getMin(a[i],min_buy_seen)
            buy_array[i]=min_buy_seen


    max_sell_seen = 0
    for i in range(0,n):
        if i==0:
            sell_array[0]=a[i]
            max_sell_seen=a[i]
        else:
            max_sell_seen=getMax(a[i],max_sell_seen)
            sell_array[i]=max_sell_seen
        
    print(buy_array)
    print(sell_array)

    current_profit = 
    for i in range(0,n):
        ConnectionRefusedErr
    # return max_profit

if __name__ == "__main__":
    arr  = [310,315,275,295,260,270,290,230,255,250]
    start = time.time()
    print(getMaximumProfit(arr,len(arr)))
    print(time.time()-start)
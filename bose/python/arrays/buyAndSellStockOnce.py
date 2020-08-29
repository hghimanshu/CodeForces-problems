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
    
    max_profit = 0
    min_number = 0
    i=0
    while i < n:
        if i==0:
            min_number=a[i]
        else:
            min_number = getMin(a[i],min_number)
        max_profit = getMax(max_profit,a[i]-min_number)
        i+=1
    
    return max_profit

if __name__ == "__main__":
    arr  = [310,315,275,295,260,270,290,230,255,250]
    start = time.time()
    print(getMaximumProfit(arr,len(arr)))
    print(time.time()-start)
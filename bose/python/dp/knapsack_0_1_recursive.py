def knapsack(wt,val,W,N):
    if N==0 or W==0:
        return 0
    if wt[N-1] <= W:
        return max(val[N-1] + knapsack(wt,val,W - wt[N-1],N-1),
                    knapsack(wt,val,W,N-1))
    elif wt[N-1] > W:
        return knapsack(wt,val,W,N-1)

if __name__ == "__main__":
    wt = [1,3,4,5]
    val =[1,4,5,7]
    W = 7
    print(knapsack(wt,val,W,len(wt)-1))


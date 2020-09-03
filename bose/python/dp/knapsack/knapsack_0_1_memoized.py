import time
import random

wt = []
val = []
i=0
while i<70:
    random_number = random.randint(1,100)
    if random_number in wt:
        continue
    else:
        wt.append(random_number)
        i+=1

i=0
while i<70:
    random_number = random.randint(1,100)
    if random_number in val:
        continue
    else:
        val.append(random_number)
        i+=1


W = 1000


# t = [[-1]*(W+1)]*(len(wt)+1))

n=len(wt)
print(n)
t = [[-1 for x in range(W+1)] for y in range(n+1)]

# print(t)

def knapsack(wt,val,W,N):
    if N==0 or W==0:
        return 0
    # print("N is::: ",N)
    # print("W is::: ",W)
    if t[N][W]!=-1:
        return t[N][W] 

    if wt[N-1] <= W:
        t[N][W] =  max(val[N-1] + knapsack(wt,val,W - wt[N-1],N-1),
                    knapsack(wt,val,W,N-1))
        return t[N][W]

    elif wt[N-1] > W:
        t[N][W] = knapsack(wt,val,W,N-1)
        return t[N][W]

if __name__ == "__main__":
    # print(t)

    # wt = [1,2,3,5]
    # val = [1,6,10,16]

    # W = 
    start_time = time.time()
    print(knapsack(wt,val,W,len(wt)-1))
    end_time = time.time() - start_time
    print(end_time)


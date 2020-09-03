import time
import random

wt = []
val = []
i=0
while i<=70:
    random_number = random.randint(1,100)
    if random_number in wt:
        continue
    else:
        wt.append(random_number)
        i+=1

i=0
while i<=70:
    random_number = random.randint(1,100)
    if random_number in val:
        continue
    else:
        val.append(random_number)
        i+=1


W = 1000


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
    val = [1,4,5,7]

    W = 7
    start_time = time.time()
    print(knapsack(wt,val,W,len(wt)-1))
    end_time = time.time() - start_time
    print(end_time)


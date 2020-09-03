import time

wt = [1,3,4,5]
val = [1,4,5,7]

W = 7


t = [[-1 for x in range(W+1)] for y in range(len(val)+1)]

def solveKnapsack(val,wt,capacity):
    return Knapsack(val,wt,capacity,0)


def Knapsack(val,wt,capacity,current_index):
    if capacity <=0 or current_index >= len(val):
        return 0

    if t[current_index][capacity] !=-1:
        return t[current_index][capacity]
    #profit1 for including the item
    
    #profit 2 is used when excluding item
    profit1 = -1
    profit2 = -1
    if wt[current_index]<=capacity:
        profit1 = val[current_index] + Knapsack(val,wt,
                                        capacity-wt[current_index],current_index+1
                                            )
        profit2 = Knapsack(val,wt,
                        capacity,current_index+1
                                        )
        t[current_index][capacity] = max(profit1,profit2)

        return t[current_index][capacity]
    
    else:
        t[current_index][capacity] = Knapsack(val,wt,
                        capacity,current_index+1
                                        )
        return t[current_index][capacity]
    # return max(profit1,profit2)


if __name__ == "__main__":


    start_time = time.time()
    print(solveKnapsack(val,wt,W))
    end_time = time.time() - start_time
    print(end_time)

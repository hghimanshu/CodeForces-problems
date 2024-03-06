def getMax(a,b):
    return max(a,b)

def maxSubArraySum(a,size):
    max_sum = 0
    max_ending_here = 0
    i=0
    while i < size:
        max_ending_here= getMax(max_ending_here+a[i],0)
        if max_ending_here>max_sum:
            max_sum = max_ending_here
        # print(max_sum)
        i+=1

    return max_sum



if __name__ == "__main__":
    a =[-2,-1]
    # a = [1,2,3,-2,5]
    print(maxSubArraySum(a,len(a)))
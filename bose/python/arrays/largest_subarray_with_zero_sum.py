def maxLen(arr):
    sum = 0
    maxi = 0
    prefix = {}
    for i in range(len(arr)):
        sum += arr[i]
        if sum==0:
            maxi =i+1
        else:
            if prefix.get(sum):
                maxi = max(maxi,i-prefix[sum])
            else:
                prefix.update({sum:i})

    return maxi

if __name__ == "__main__":
    arr = [1,-1,3,2,-2,-8,1,7,10,23]
    print(maxLen(arr))
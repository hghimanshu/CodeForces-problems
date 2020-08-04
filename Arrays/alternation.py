def alternation(arr):
    for i in range(len(arr)):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=i%2)
    
    return arr

arr = [1,2,4,6,3,56,878,21, 7]
print(alternation(arr))
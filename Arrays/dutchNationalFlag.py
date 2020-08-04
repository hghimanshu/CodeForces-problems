def sortArr(arr, n):
    pivot = arr[n]
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller +=1
    
    larger = len(arr) -1
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -=1
    

    return arr


arr = [0, 1, 1, 0, 0, 2, 1, 2, 1, 0, 0, 1] 
pivot = 5
print(sortArr(arr, pivot)) 
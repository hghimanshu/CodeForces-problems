def waveTransform(arr):
    n = len(arr)

    for i in range(n):
        arr[i:i+2] = sorted(arr[i:i+2], reverse=(i+1)%2)
        print(arr)
    return arr


a = [1,2,3,4,5]

print(waveTransform(a))
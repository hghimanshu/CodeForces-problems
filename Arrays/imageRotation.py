def rotateImage(arr):
    n = len(arr)
    result = []
    it = 0
    

    for i in list(reversed(range(n))):
        row = 0
        ans = []
        for j in range(n):
            ans.append(arr[i + row][it])
            row -=1
        it +=1
        result.append(ans)
    
    return result



arr = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(rotateImage(arr))
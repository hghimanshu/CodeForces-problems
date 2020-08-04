def deleteDuplicateFromArray(arr):
    new_arr = [0]*len(arr)
    i = 0
    for j in arr:
        if not j in new_arr:
            new_arr[i] = j
            i+=1
    return new_arr




arr = [2,3,5,5,7,11,11,11,13]
print(deleteDuplicateFromArray(arr))
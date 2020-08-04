def sortArr(arr, n):
    count_each_element = [(i, arr.count(i)) for i in arr]
    count_each_element = list(set(count_each_element))
    count_each_element = sorted(count_each_element, key= lambda x: x[0])

    j = 0

    for i in range(len(count_each_element)):
        current_val, current_val_count = count_each_element[i]
        
        while current_val_count > 0:
            arr[j] = current_val
            j +=1
            current_val_count -=1

    return arr


arr = [0, 1, 1, 3, 3, 2, 1, 2, 1, 0, 0, 1] 
pivot = 2
print(sortArr(arr, pivot)) 
def logic(arr):
    arr[-1] +=1
    carry = 0
    l = len(arr)
    for i in reversed(range(len(arr))):
        if arr[i] == 10:
            arr[i] = 0
            carry +=1
        else:
            arr[i] +=carry
            carry = 0
            if arr[i] == 10:
                arr[i] = 0
                carry +=1
    
    if arr.count(0) == l:
        return [1] + arr
    return arr



a = [9,9,9,9,9]
print(logic(a))
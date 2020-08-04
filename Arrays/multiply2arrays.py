def multiplyArrays(arr1, arr2):
    sign = -1 if (arr1[0] <0  or arr2[0] < 0 )else 1
    arr1[0], arr2[0] = abs(arr1[0]), abs(arr2[0])

    result = [0] * (len(arr1) + len(arr2))

    for i in reversed(range(len(arr1))):
        for j in reversed(range(len(arr2))):
            result[i+j+1] += arr1[i]* arr2[j]
            result[i+j] += result[i+j+1]//10
            result[i+j+1] %=10
    
    result = result[next((i for i, x in enumerate(result) if x !=0), len(result)):] or [0]
    return [sign * result[0] ] + result[1:]




arr1 = [1,9,3,7,0,7,7,2,1]
arr2 = [-7,6,1,8,3,8,2,5,7,2,8,7]
print(multiplyArrays(arr1, arr2))
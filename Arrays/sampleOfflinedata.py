from random import randint

def offlineData(arr, k):
    # if k <= 1:
    #     return arr[randint(0, len(arr))]
    # else:
    #     end_ptr = len(arr) - 1
    #     for i in range(k):
    #         random_val = randint(0, end_ptr)
    #         arr[end_ptr], arr[random_val] = arr[random_val], arr[end_ptr]
    #         end_ptr -=1
    # return arr[end_ptr + 1:len(arr) - 1] 
    for i in range(k):
        val = randint(i, len(arr) -1)
        arr[i], arr[val] = arr[val], arr[i]
    return arr


arr = [1,2,3,4,5,6,7,8,9]
k = 2

print(offlineData(arr, k))
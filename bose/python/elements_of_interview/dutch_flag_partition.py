

def arrange(arr):
    arr_less=[]
    arr_grt=[]
    for i in range(0,len(arr)):
    #     print('\npivot is:: ',pivot)
    #     print('current number is::: ',arr[i])
        if arr[i]>pivot:
            arr_grt.append(arr[i])
        else:
            arr_less.append(arr[i])
    return arr_less+arr_grt

def arrange_2(arr,pivot):
    smaller =0
    for i in range(0,len(arr)):
        if arr[i]<pivot:
            arr[i],arr[smaller] = arr[smaller],arr[i]
            smaller+=1
    larger = len(arr)-1
    for i in reversed(range(0,len(arr))):
        if arr[i]<pivot:
            break
        if arr[i]>pivot:
            arr[i],arr[larger] = arr[larger],arr[i]
            larger-=1
    print(arr)

def dutch_flag(a,pivot):
    smaller,equal,larger = 0,0,len(a)
    while equal < larger:
        if a[equal] < pivot:
            a[smaller],a[equal] = a[equal],a[smaller]
            smaller,equal = smaller+1,equal+1
        elif a[equal] == pivot:
            equal+=1
        elif a[equal] > pivot:
            larger-=1
            a[larger],a[equal] = a[equal],a[larger]
            # smaller,equal = smaller+1,equal+1
    print(a)


if __name__ == "__main__":
    a =[0,1,2,0,2,1,1]
    pivot_index = 3
    pivot = a[pivot_index]
    dutch_flag(a,pivot)
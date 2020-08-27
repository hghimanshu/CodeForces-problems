
def thirdLargest(arr, n):
    # code here
    if n<3:
        return -1
    first =0
    second =0
    third =0
    for i in range(0,n):
        if arr[i]>=first:
            third = second
            second = first
            first= arr[i]
            
        elif arr[i]>=second and arr[i] < first:
            third = second
            second = arr[i]
        
        elif arr[i] < second and arr[i]>=third:
            third = arr[i]
    print("First is:: ",first)
    print("second is:: ",second)
    print("third is:: ",third)
    return third

if __name__ == "__main__":
    a =[18,21,10,24,27,5]
    print(thirdLargest(a,len(a)))
    
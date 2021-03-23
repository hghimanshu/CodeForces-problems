def remove_dup(arr):
    i=0
    last_found=0
    while i<len(arr):
        if arr[i]!=last_found:
            last_found = arr[i]
        else:
            last_found =a[i]
            arr[i]=0
        i+=1

    i=0
    zero=False
    while i<len(arr):
        if arr[i]==0:
            start_idx=i
            zero=True
            i+=1

        elif arr[i]!=0:
            if zero:
                arr[start_idx]=arr[i]
                zero=False
                arr[i]=0
            else:
                i+=1
    return arr
            
            
if __name__ == '__main__':
    a = [2,3,5,5,7,11,11,11,13]
    print(remove_dup(a))
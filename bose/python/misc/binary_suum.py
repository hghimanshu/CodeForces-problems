def binary_sum(arr,start,stop):
    if start >= stop:
        return 0
    elif start==stop-1:
        return arr[start]
    else:
        mid = int((stop+start)/2)
        return binary_sum(arr,start,mid) + binary_sum(arr,mid,stop)
    
    

a = [1,2,3,4,5,6,7,8]

print(binary_sum(a,0,len(a)))
import sys
def binary_search(arr,low,high,data):
    mid = int((low+high)/2)
    if data == arr[mid]:
        return True
    if low==mid or low > high:
        return False
    if data < arr[mid]:
        return binary_search(arr,low,mid,data)
    if data > arr[mid]:
        return binary_search(arr,mid,high,data)
    
    


arr = [2,4,5,6,7,8,9,10,11,12,13,14]
print(binary_search(arr,0,len(arr)-1,int(sys.argv[1])))

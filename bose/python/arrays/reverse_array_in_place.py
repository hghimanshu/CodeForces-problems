from typing import List

def reverse_array(arr:List[int]):
    i: int = 0
    j: int = len(arr)-1
    
    while(i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i+=1
        j-=1
    return arr

if __name__=="__main__":
    nums = [1,2,3,4,5,6,7]
    print(reverse_array(nums))
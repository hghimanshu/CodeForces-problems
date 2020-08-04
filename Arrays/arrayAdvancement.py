def arrayAdvancement(arr):
    reach_so_far, lastIndex = 0, len(arr) -1
    i = 0
    while i <= reach_so_far and reach_so_far < lastIndex:
        reach_so_far = max(reach_so_far, arr[i] + i)
        i+=1
    
    return reach_so_far >= lastIndex
         

arr = [3,3,1,0,2,0,1]
print(arrayAdvancement(arr))
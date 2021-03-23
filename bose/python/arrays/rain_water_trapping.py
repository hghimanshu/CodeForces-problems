def find_start_pos(arr):
    i=0
    while i < len(arr):
        if arr[i]==0:
            i+=1
            continue
        if arr[i]!=0:
            break
def trap_sub_optimal(arr):

    '''Water to be stored at any index is 
    min(Max(left height for that index),Max(right height for that index))-height[i]'''

    left_arr = [0]*len(arr)
    right_arr = [0]*len(arr)

    max_left =0
    max_right =0
    for i in range(0,len(arr)):
        left_arr[i]= max(max_left,arr[i])
        max_left = left_arr[i]

    for i in reversed(range(len(arr))):
        right_arr[i]= max(max_right,arr[i])
        max_right = right_arr[i]

    print(left_arr)
    print(right_arr)

    total_water =0

    for i in range(0,len(arr)):
        total_water+= min(left_arr[i],right_arr[i])-arr[i]
    
    return total_water

def trap_water_optimal(height):
    total_water = 0
    left_max = 0
    right_max = 0

    l=0
    r = len(height)-1

    while l < r:
        if height[l] <= height[r]:
            if height[l] >= left_max:
                left_max = height[l]
            else:
                total_water+=left_max-height[l]
            l+=1
        else:
            if height[r] >= right_max:
                right_max = height[r]
            else:
                total_water+=right_max-height[r]
            r-=1

    return total_water

if __name__ == '__main__':
    arr = [4,2,0,3,2,5]
    # arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(trap_water_optimal(arr))

def get_max_area(arr):
    '''Returns the max area in O(n^2) time complexity.Fails time constraint requirement on leetcode'''
    max_area =0
    for first in range(0,len(arr)):
        for second in range(first+1,len(arr)):
            base = second-first
            curr_area = min(arr[first],arr[second])*base
            max_area = max(max_area,curr_area)

    return max_area

def get_max_area_two_pointer(height):
    '''Two pointer approach'''
    max_area = 0
    i=0
    j= len(height)-1
    while i<j:
        base = j-i
        curr_area = min(height[i],height[j])*base
        max_area = max(max_area,curr_area)

        if height[i]<height[j]:
            i+=1
        elif height[i]>height[j]:
            j-=1
        else:
            i+=1
            j-=1

    return max_area

if __name__ == "__main__":
    array = [1,8,6,2,5,4,8,3,7]
    # array = [4,3,2,1,4]
    # array = [1,2,1]
    print(get_max_area_two_pointer(array))
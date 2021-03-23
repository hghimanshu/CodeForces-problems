

def check(idx,arr):
    curr = idx

    if curr>=len(arr)-1:
        return 1

    if arr[idx]==0:
        return 0
    
    max_val = arr[curr]

    
    while max_val:
        x = check(curr+max_val,arr)
        if not x:
            max_val-=1
        else:
            return 1
    return 0

if __name__ == "__main__":
    # a = [3,3,1,0,2,0,1]
    # a = [3,2,0,0,2,0,1]
    a = [2,4,1,1,0,2,3]
    if check(0,a):
        print("We can reach last position")
    else:
        print("We cannot reach last position")

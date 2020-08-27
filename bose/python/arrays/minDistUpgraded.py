def getDistance(index1,index2):
    if index1==-1 or index2==-1:
        return -1
    return abs(index2-index1)

def minDist(arr, n, x, y):
    # Code here

    if x not in arr or y not in arr:
        return -1
        
    if n==1:
        return -1
    if n==2:
        return 1

    for i in range(0,n):

        if arr[i]==x:
            num1=x
            num2=y
            start_index = i
            break
        elif arr[i]==y:
            num1=y
            num2=x
            start_index = i
            break
    
    j=0
    idx1=-1
    idx2=-1
    min_dist=-1
    while j< n:
        if arr[j]==x:
            idx1=j
            if min_dist==-1:
                min_dist = getDistance(idx1,idx2)
            else:
                min_dist=min(getDistance(idx1,idx2),min_dist)
        if arr[j]==y:
            idx2=j
            if min_dist==-1:
                min_dist=getDistance(idx1,idx2)
            else:
                min_dist=min(getDistance(idx1,idx2),min_dist)
        j+=1

    return min_dist

if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,8,9,10,6,12,67]
    arr = [1,2,3,4,5,6,7,6,12,9,90,67,6,9]
    print(minDist(arr,len(arr),6,9))

# 98 78 10 12 59 37 45 18 1 56 37 14 3 32 85 10 69 89 29 93 44 16 26 13 50 75 79 21 20 33 55 17 63 64 80 21 52 24 90 52 80 26 18 34 57 2 95 25 42 23 17 85 39 94 50 40 21 28 12 40 61 67 9 23 30 88 95 34 64 85 85 95 62 54 28 19 55 22 95 49 97 64 33

# 96 82 48 76 34 19 7 80 36 57 77 34 19 35 5 57 16 66 42 62 89 19 60 19 25 16 20 51 77 75 12 73 8 11 100 93 81 58 72 17 14 48 2 33 82 6 41 49 72 34 10 12 53 21 30 77 36 49 79 13 75 42
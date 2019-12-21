def processArray(arr):
    val = checkSort(arr)
    return val

def checkSort(arr):
    if arr == sorted(arr):
        return len(arr)
    else:
        n = len(arr) // 2
        val1 = processArray(arr[:n])
        val2 = processArray(arr[n:])
        return max(val1,val2)

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split(' ')))
    ans = checkSort(arr)
    print(ans)
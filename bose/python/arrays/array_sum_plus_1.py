def get_incremented_number(arr):
    arr.reverse()
    carry=1
    for i in range(0,len(arr)):
        if arr[i]+carry==10:
            if i==len(arr)-1:
                arr.append(1)
            arr[i] = 0
        else:                                                                                                                                            
            arr[i]+=carry
            break
    arr.reverse()
    return arr

if __name__ == "__main__":
    arr = [9,9,9]
    print(get_incremented_number(arr))
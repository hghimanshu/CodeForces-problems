def deleteDup(arr):
    dupDict = {}
    for i in range(0,len(arr)):
        if arr[i] not in dupDict:
            dupDict.update({arr[i]:1})
            arr[i]=0
        else:
            dupDict[arr[i]]+=1
            arr[i]=0
    # print(dupDict)
    # print(arr)

    keyList = list(dupDict.keys())
    for i in range(0,len(keyList)):
        arr[i] = keyList[i]

    return arr

if __name__ == "__main__":
    arr =[2,3,5,5,7,11,11,11,13]
    print(deleteDup(arr))
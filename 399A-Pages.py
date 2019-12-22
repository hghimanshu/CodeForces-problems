def addingSymbols(string, n, val):
    if len(string) != 0:
        if val == "front":
            if int(string.split(' ')[0]) == 1:
                return string
            elif int(string.split(' ')[0]) < 1:
                return " ".join([str(i) for i in string.split(' ') if int(i) >= 1])
            else:
                return "<< " + string 
        else:
            if int(string.split(' ')[-1]) == n:
                return string
            elif int(string.split(' ')[-1]) > n:
                return " ".join([str(i) for i in string.split(' ') if int(i) <= n])
            else:
                return string + " >>"
    else:
        return string

def navigationPage(n, p, k, val):
    l = []
    if val == "sub":
        while k != 0:
            if p > 1:
                l.append(p-k)
            else:
                l = []
            k -=1
    else:
        while k != 0:
            if p <= n:
                l.append(p+k)
            else:
                l = []
            k -=1
        l.sort()
    return " ".join([str(i) for i in l])

def calculateReq(n,p,k):
    prev_ = navigationPage(n, p, k, "sub") 
    next_ = navigationPage(n, p, k, "add")
    prev_ = addingSymbols(prev_, n, "front")
    next_ = addingSymbols(next_, n, "back")
    answer = prev_ + " (" + str(p) + ") " + next_
    return answer.strip()

if __name__ == "__main__":
    n,p,k = map(int, input().split(' '))
    answer = calculateReq(n,p,k)
    print(answer)
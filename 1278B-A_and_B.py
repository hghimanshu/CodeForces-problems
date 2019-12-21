
# def findSmallNo(a,b):
#     if a > b:
#         return b
#     else:
#         return a


def add(a,b):
    iteration = 0

    while True:
        if a == b:
            return iteration
        else:   
            diff = abs(a - b)
            if a > b:
                leng = a
            else:
                leng = b
            for i in range(1, leng):




if __name__ == "__main__":
    
    outputs = []
    # t = int(input())
    t = 1
    for i in range(t):
        a, b = 1, 3
        # a, b = map(int, input().split(' '))
        # print(a,b)
        ans = add(a,b)
        outputs.append(ans)

    for i in outputs:
        print(i)

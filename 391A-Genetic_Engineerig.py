import itertools

if __name__ == "__main__":
    s = input()
    z = [(x[0], len(list(x[1]))) for x in itertools.groupby(s)]
    count = 0
    for i in z:
        if i[1] %2 ==0:
            count +=1
    print(count)
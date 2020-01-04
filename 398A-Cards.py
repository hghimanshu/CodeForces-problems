import itertools

if __name__ == "__main__":
    # a, b = map(int, input().split(' '))
    a, b = 2, 3
    total_o = "".join(list(map(lambda x:'o', list(range(a)))))
    total_x = "".join(list(map(lambda x:'x', list(range(b)))))
    total_perm = list(set(itertools.permutations(total_o + total_x)))
    calc = {}
    for i in total_perm:
        sum_ = 0
        i = "".join(i)
        for x in itertools.groupby(i):
            if x[0] == 'o':
                sum_ += len(list(x[1]))**2
            else:
                sum_ -= len(list(x[1]))**2
        calc[i] = sum_
    print(max(calc.values()))
    print(max(calc.keys()))
    print(calc)
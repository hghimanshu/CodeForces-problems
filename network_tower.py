t = int(input())
for _ in range(t):
    x = list(map(int, input().split(',')))
    h = list(map(int, input().split(',')))    

for i in range(len(x)):
    aff = x[i] + h[i]
    for j in range(i+1, len(x)):
        if x[j] <= aff:
            aff = x[j] + h[j]
            continue
        else:
            break
    print(aff)
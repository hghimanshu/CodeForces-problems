import time
import random

wt = []
val = []
i=0
while i<=100:
    random_number = random.randint(1,300)
    if random_number in wt:
        continue
    else:
        wt.append(random_number)
        i+=1
i=0
while i<=100:
    random_number = random.randint(1,300)
    if random_number in val:
        continue
    else:
        val.append(random_number)
        i+=1

n = len(val)
W = 1000

t = [[-1 for x in range(W+1)] for y in range(n+1)]

# print(t)

# print("/n/n")

#initialization step based on recursive base condition

for i in range(0,n):
    t[i][0] = 0

for j in range(0,W+1):
    t[0][j] = 0
# print(t)

# print(t)

# print("/n/n")

start_time = time.time()
for i in range(1,n):
    for j in range(1,W+1):
        if wt[i-1] <= W:
            t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]],
                        t[i-1][j]
                        )
        elif wt[i-1] > W:
            t[i][j] = t[i-1][j]

# print(t)
# print("/n/n")

print(t[n-1][W-1]) 
end_time = time.time() - start_time
print(end_time)

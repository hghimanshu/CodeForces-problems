#code
# for _ in range(int(input())):
x1,y1,x2,y2 = 1,1,10,1
x3,y3,x4,y4 = 1,2,10,2

A1 = y2 - y1
B1 = x1 - x2
C1 = A1*x + B1*y

A2 = y4 - y3
B2 = x3 - x4
C2 = A2*x + B2*y

x = (B2*C1 - (B1*C2))/(A1*B2 - A2*B1)

y = (C1 - (A1*x))/B1

print(x,y)
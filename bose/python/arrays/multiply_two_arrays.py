# x = [1,9]
# y = [-7,6,1]

x=[1,9,3,7,0,7,7,2,1]
y=[-7,6,1,8,3,8,2,5,7,2,8,7]

result = [0]*(len(x)+len(y))
print(result)

##get sign
def get_sign(x,y):
    if x[0]>0 and y[0]>0:
        return 1
    else:
        return -1
carry=0
for i in reversed(range(len(x))):
    for j in reversed(range(len(y))):
        value = abs(x[i])*abs(y[j])
        print(value)
        result[i+j+1]+=value
        carry=result[i+j+1]//10
        result[i+j]+=carry
        result[i+j+1]=result[i+j+1]%10

print(result)

# for i in range(0,len(result)):
#     result[i]/=10**i
# print("Updated result is :: {}".format(result))

# ##put appropriate sign
sign = get_sign(x,y)
result[0]*=sign

print("Updated result is :: {}".format(result))

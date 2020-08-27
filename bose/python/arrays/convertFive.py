def convertFive(n):
    # Code here
    num_list =[]
    while n>=10:
        last_digit = n%10
        if last_digit==0:
            num_list.append(str(5))
        else:
            num_list.append(str(last_digit))
        n = int(n/10)
    num_list.append(str(n))
    num_list.reverse()
    num = "".join(num_list)
    return int(num)

    # for idx in range(0,len(num_str)):
    #     if num_str[idx]=="0":
    #         num_str[idx]="5"
    # return int(num_str)

if __name__ == "__main__":
    print(convertFive(10000))
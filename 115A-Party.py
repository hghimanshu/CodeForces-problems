if __name__ == "__main__":
    n = int(input())
    ans = 0
    mem = []
    for i in range(n):
        mem.append(int(input()))
    for i in range(n):
        count = 0
        x = mem[i]
        while x != -1:
            x = mem[x-1]
            count +=1
        ans = max(ans, count)
    print(ans +1)
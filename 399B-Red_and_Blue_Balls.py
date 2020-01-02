if __name__ == "__main__":
    n = int(input())
    balls = str(input())
    ans = sum(2 ** i for i in range(n) if balls[i] == 'B')
    print(ans)
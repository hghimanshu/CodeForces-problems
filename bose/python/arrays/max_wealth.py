def maximumWealth(accounts):
    max_wealth=0
    print(accounts)
    for i in range(0,len(accounts)):
        total = 0
        for j in range(0,len(accounts)):
            print("Current wealth is :: {}".format(accounts[i][j]))
            total+=accounts[i][j]
        max_wealth = max(total,max_wealth)
    return max_wealth

if __name__ == '__main__':
    accounts = [[1,2,3],[3,2,1]]
    print(maximumWealth(accounts))
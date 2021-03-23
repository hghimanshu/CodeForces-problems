def change_making(cents):
    '''Time complexity is O(1)'''
    
    COINS = [100,50,25,10,5,1]
    total_change = 0
    for coin in COINS:
        total_change += cents // coin
        cents %= coin
    
    return total_change

if __name__ == '__main__':
    cents = 526
    print("Total change is :: {}".format(change_making(cents)))
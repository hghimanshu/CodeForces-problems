if __name__ == "__main__":
    s = input()
    map_ = {'n': 0, 'i': 0, 'e': 0, 't': 0}

    for ch in s:
        if ch in map_.keys():
            map_[ch] +=1
    
    ans = map_['i']
    ans = min(ans, map_['t'])
    ans = min(ans, (map_['n'] -1 )/2)
    ans = min(ans, map_['e']/3)
    print(int(ans))
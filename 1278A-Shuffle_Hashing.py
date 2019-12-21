import string 
import random 
import time 
    	
    
def countForEachChar(string):
    dic = {}
    for i in list(string):
        if not i in dic.keys():
            dic[i] = list(string).count(i)
    return dic

def traversing(given_hash, map_, string):
    for s in range(len(given_hash)):
        if given_hash[s] in map_.keys():
            copy_map = map_.copy()
            for i in range(s, len(given_hash)):
                if given_hash[i] in copy_map.keys():
                    copy_map[given_hash[i]] -= 1

                    if copy_map[given_hash[i]] == 0:
                        del copy_map[given_hash[i]]

                if list(copy_map.keys()) == []:
                    return "YES"

    if list(copy_map.keys()) != []:
        return "NO"


def checkingHash(string, given_hash):
    map_ = countForEachChar(string)
    answer = traversing(given_hash, map_, string)
    print(answer)

if __name__ == "__main__":
    
    inputs = {}

    t = int(input())
    for i in range(t):
        s = str(input())
        h = str(input())
        inputs[s] = h
    for i in inputs.keys():
        checkingHash(i,inputs[i])
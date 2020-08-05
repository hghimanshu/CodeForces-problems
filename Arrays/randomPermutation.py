from itertools import permutations


def getPermutations(n):
    arr = list(range(n))
    arr = list(permutations(arr, n))
    return arr

n = 6
print(getPermutations(n))
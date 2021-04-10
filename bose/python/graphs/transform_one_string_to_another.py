import string
def transform_string(D,s,t):
    q = [(s,0)] 
    ''' This queue contains a tuple. The first character in the tuple is the string.
                     the second character is the distance from input string to'''


    ''' In order to mark the string as visited
    we remove it from D''' 
    D.remove(s)
    visited = [(s,0)]
    while len(q):
        f = q.pop(0)

        if f[0] == t: #dest string found
            print(visited)
            return f[1]
        
        ''' We try all possible single character transformations possible 
        on s by iterating through all indices and all values from a ~ z'''

        for i in range(0,len(s)):
            for c in string.ascii_lowercase:
                cand = f[0][:i] + c + f[0][i+1:]
                if cand in D:
                    D.remove(cand)
                    q.append((cand,f[1]+1))
                    visited.append((cand,f[1]+1))
    print(visited)
    return -1

if __name__ == "__main__":
    D = ["bat","cot","dog","dag","dot","cat"]
    s = "cat"
    t = "dog"
    print(transform_string(D,s,t))
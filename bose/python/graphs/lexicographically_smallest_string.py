class FindSmallestString:

    def __init__(self):
        self.min_str = ""


    def add(self,a,s):
        new_string = ""
        for i in range(0,len(s)):
            if i%2!=0:
                new_string+= str((int(s[i]) + a)%10)
            else:
                new_string+=s[i]
        return new_string

    def rot(self,b,s):
        return s[len(s)-b:] + s[:len(s)-b]

    def dfs(self,a,b,s,visited):
        if visited.get(s,0):
            return
        visited.update({s:True})
        if not self.min_str:
            self.min_str =s
        else:
            self.min_str=min(self.min_str,s)
        self.dfs(a,b,self.add(a,s),visited)
        self.dfs(a,b,self.rot(b,s),visited)

    def bfs(self,a,b,s):
        q=[s]
        visited={}
        while len(q)!=0:
            x=q.pop(0)
            if visited.get(x,0):
                continue
            visited.update({x:True})
            if not self.min_str:
                self.min_str =s
            else:
                self.min_str=min(self.min_str,x)
            q.append(self.add(a,s))
            q.append(self.rot(b,s))
            



    def findLexSmallestString(self, s, a, b):
        self.bfs(a,b,s)
        return self.min_str
             




if __name__ == "__main__":
    obj = FindSmallestString()
    s = "5525"
    a = 9
    b = 2
    print("Smallest string is :: {}".format(obj.findLexSmallestString(s,a,b)))
class Solution:

    def __init__(self):
        self.sets = []


    def getCombinations(self,curr,n,chars):
        if len(curr)==n:
            # self.sets.add("".join(curr))
            self.sets.append("".join(curr))
            return 

        for i in range(0,len(chars)):
            if len(curr)>0 and chars[i]==curr[-1]:
                continue
            
                # visited[i] = True
            curr.append(chars[i])
            self.getCombinations(curr,n,chars)
            curr.pop()
                # visited[i] = False

    
    def getHappyString(self, n, k):

        chars = ['a','b','c']


        self.getCombinations([],n,chars)
        # print(self.sets)
        if k>len(self.sets):
            return ""
        else:
            # return list(self.sets)[k]
            return self.sets[k-1]

if __name__ == "__main__":
    sol = Solution()
    n=10
    k=100
    print(sol.getHappyString(n,k))
class Solution:

    def __init__(self):
        self.cache = {}
        self.vowels = ["a","e","i","o","u"]
        

    def getStrings(self,n,char,idx):

        if n-1==0:
            return 1

        if char+"_"+str(n) in self.cache:
            return self.cache[char+"_"+str(n)]

        totalStrings = 0

        for i in range(idx,len(self.vowels)):
            totalStrings += self.getStrings(n-1,self.vowels[i],i)

        self.cache[char+"_"+str(n)] = totalStrings
        return totalStrings

    def countVowelStrings(self, n):
        for i in range(0,len(self.vowels)):
            self.getStrings(n,self.vowels[i],i)

        totalSum=0
        for string in self.vowels:
            totalSum+= self.cache[string+"_"+str(n)]
        
        return totalSum


if __name__ == "__main__":
    sol = Solution()
    sol.countVowelStrings(33)
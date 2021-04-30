class Solution:

    def __init__(self):
        self.sets = set()
        self.vowels = ["a","e","i","o","u"]

    def getStrings(self,curr,n,idx):
        if len(curr)==n:
            self.sets.add(curr)
            return

        

        for i in range(idx,len(self.vowels)):
            curr+=self.vowels[i]
            if len(curr) > n:
                return
            self.getStrings(curr,n,i)
            curr=curr[:-1]


    def countVowelStrings(self, n):
        for i in range(0,len(self.vowels)):
            self.getStrings(self.vowels[i],n,i)

        # print("Sets are :: {}".format(self.sets))
        return len(self.sets)

if __name__ == "__main__":
    sol = Solution()
    n = 33
    print(sol.countVowelStrings(n))
class Solution:

    def __init__(self,characters,combinationLengths):
        self.sets = []
        self.characters =  characters
        self.combinationLengths = combinationLengths

        self.getAllCombinations()

    def next(self):
        if len(self.sets) >0:
            return self.sets.pop(0)
        else:
            return []

    def hasNext(self):
        if len(self.sets) == 0:
            return False
        return True

    def getComb(self,curr,idx):
        if len(curr)==self.combinationLengths:
            self.sets.append(curr)
            return
        
        for i in range(idx+1,len(self.characters)):
            curr+=self.characters[i]
            if len(curr) > self.combinationLengths:
                curr = curr[0:-1]
                continue
            else:
                self.getComb(curr,i)
                curr = curr[:-1]
    
    def getAllCombinations(self):
        for i in range(0,len(self.characters)):
            self.getComb(self.characters[i],i)
    

if __name__ == "__main__":
    characters = "abc"
    combinationLengths = 2

    sol = Solution(characters,combinationLengths)
    print(sol.next())
    print(sol.hasNext())
    print(sol.next())
    print(sol.hasNext())
    print(sol.next())
    print(sol.hasNext())



    

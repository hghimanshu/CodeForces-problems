class Solution:
    
    def __init__(self):
        self.sets =  set()
        self.ascii_vals = [i for i in range(65,123)]
        self.upper = [i for i in range(65,91)]
    

    def toggleChar(self,char):
        if ord(char) in self.upper:
            return char.lower()
        else:
            return char.upper()

    def getCombination(self,comb,idx):
        string = "".join(comb)
        self.sets.add(string)

        for i in range(idx,len(comb)):
            if ord(comb[i]) in self.ascii_vals:
                comb[i] = self.toggleChar(comb[i])
                if not "".join(comb) in self.sets:
                    self.getCombination(comb,i+1)
                comb[i] = self.toggleChar(comb[i])
        return

    def letterCasePermutation(self, S):
        self.getCombination(list(S),0)

        print(self.sets)

if __name__ == "__main__":
    S = "A1B2"

    sol =Solution()
    sol.letterCasePermutation(S)
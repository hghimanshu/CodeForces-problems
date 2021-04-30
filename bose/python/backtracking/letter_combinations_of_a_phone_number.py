class Solution:
    def __init__(self):
        self.sets= set()
        self.telephone = {
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
    

    def getCombinations(self,comb,idx,nums):
        if len(comb)==len(nums):
            self.sets.add("".join(comb))
            return

        for letter in self.telephone[nums[idx]]:
            comb.append(letter)
            self.getCombinations(comb,idx+1,nums)
            comb.pop()
    
    def letterCombinations(self, digits):
        nums = [int(i) for i in digits]

        self.getCombinations([],0,nums)
        print(self.sets)


if __name__ == "__main__":
    sol = Solution()
    digits = "234"
    sol.letterCombinations(digits)
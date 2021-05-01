class Solution:

    def __init__(self):
        self.sets = []


    def getCombination(self,curr,chars):
        if len(chars) == 0:
            self.sets.append(curr)
            return

        if len(chars) == 1:
            self.sets.append(curr+[chars])
            return

        for i in range(1,len(chars)+1):
            new_partition = chars[:i]
            if new_partition == new_partition[::-1]:  #partition check
                self.getCombination(curr+[new_partition],chars[i:])



    def partition(self,s):
        self.getCombination([],s)

        return self.sets


if __name__ == "__main__":
    sol = Solution()
    s= "a"
    print(sol.partition(s))
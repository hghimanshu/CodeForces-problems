class Solution:

    def __init__(self):
        self.sets = []
        self.ans = 0


    def getCombinations(self,chars):
        # if sub in self.sets:
        #     return False
        # else:
        if len(chars)==0:
            self.ans = max(self.ans,len(self.sets))
            # return True
        
        for i in range(1,len(chars)+1):
            string,rem = chars[:i],chars[i:]
            if string not in self.sets:
                self.sets.append(string)
            else:
                continue
            self.getCombinations(rem)
            # if check:
            #     return True
            # else:
            self.sets.pop()
        # return False


    def maxUniqueSplit(self, s):
        self.getCombinations(s)

        print("Substring length is ::{}".format(self.ans))


    def maxUniqueSplit2(self, s):
        def findMaxSize(s):
            if not s:
                self.ans = max(self.ans, len(seen))
            for i in range(1, len(s) + 1):
                print(seen)
                if s[:i] not in seen:
                    seen.add(s[:i])
                    findMaxSize(s[i:])
                    seen.remove(s[:i])
        seen = set()
        self.ans = 0
        findMaxSize(s)
        return self.ans


if __name__ == "__main__":
    sol = Solution()
    s = "wwwzfvedwfvhsww"
    sol.maxUniqueSplit(s)
from functools import lru_cache
import time
class Solution:


    def __init__(self):
        self.all_substrings = []


    def isPalDp(self,string):

        row = [False]*len(string)
        dp =[row.copy() for i in range(len(string))]
        true_count =0
        # print(dp)

        for x in range(0,len(string)):
            j=x
            for i in range(0,len(string)):
                val = string[i:x+i+1]
                # print("substr is:: {} and i is {} and j is {}".format(val,i,j))
                if val[0]==val[-1]:
                    if len(val)==1:
                        dp[i][j] = True
                    elif len(val)==2:
                        dp[i][j] = True
                    else:
                        if dp[i+1][j-1]:
                            dp[i][j] = True
                j+=1
                if j>=len(string):
                    break

        for i in range(0,len(string)):
            for j in range(0,len(string)):
                if dp[i][j]:
                    true_count+=1
        
        return true_count
        
    def isPal(self,string):

        if len(string) == 1:
            return True
        
        i=0
        j= len(string)-1

        while i<j:
            if string[i] == string[j]:
                i+=1
                j-=1

            else:
                return False
        
        return True

    @lru_cache
    def getSubstring(self,substr,idx):

        if idx >= len(self.orig_string):
            return

        new_str = substr+self.orig_string[idx]

        if self.isPal(new_str):
            self.all_substrings.append(new_str)


        self.getSubstring(new_str,idx+1)

    
    def countSubstrings(self, s):
        self.orig_string = s
        # for i in range(0,len(s)):
        #     self.getSubstring("",i)

        # return self.all_substrings
        return self.isPalDp(self.orig_string)

if __name__ == "__main__":
    sol = Solution()
    s = "aba"
    start = time.time()
    print(sol.countSubstrings(s))
    print(time.time() - start)
        
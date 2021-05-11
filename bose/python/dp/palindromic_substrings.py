from functools import lru_cache
import time
class Solution:


    def __init__(self):
        self.all_substrings = []

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
        for i in range(0,len(s)):
            self.getSubstring("",i)

        return self.all_substrings

if __name__ == "__main__":
    sol = Solution()
    s = "aaa"
    start = time.time()
    print(sol.countSubstrings(s))
    print(time.time() - start)
        
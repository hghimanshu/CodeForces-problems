from functools import lru_cache
class Solution:


    def lcs_dp(self,s1,s2):
        dp =[]
        row = [""]*(len(s1)+2)
        for i in range(0,len(s2)+2):
            dp.append(row.copy())
        # print(dp)
        # print(dp[0][2])
        for i in range(0,len(s1)):
            dp[0][i+2] = s1[i]

        for i in range(0,len(s2)):
            dp[i+2][0] = s2[i]
        # print(dp)

        rows = len(dp)
        cols = len(dp[0])

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if dp[i][0] == "" or dp[0][j] == "":
                    dp[i][j] =0
                elif dp[i][0] == dp[0][j]:
                    dp[i][j] = 1 + dp[i-1][j-1]

                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[rows-1][cols-1]

    @lru_cache
    def lps(self,string):

        if len(string)==1:
            return 1
        
        # elif string=="":
        #     return 0

        elif string[0] == string[-1]:
            if len(string[1:-1])==1:
                return 3
            return 1 + max(self.lps(string[0:-1]),self.lps(string[1:]))


        else:
            return max(self.lps(string[0:-1]),self.lps(string[1:]))



    def longestPalindromeSubseq(self, s):
        if len(s)==1:
            return 1
        if len(s)==0:
            return 0
        return self.lcs_dp(s,s[::-1])

    

if __name__ == "__main__":
    sol = Solution()
    s = "bbb"
    print(sol.longestPalindromeSubseq(s))
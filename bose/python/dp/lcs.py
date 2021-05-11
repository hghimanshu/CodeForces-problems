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
    def lcs_rec(self,s1,s2):
        print("S1 is {} and S2 is {}".format(s1,s2))

        if s1=="" or s2=="":
            return 0

        if s1[-1]==s2[-1]:
            print("Found match")
            # s1=s1[0:-1]
            # s2= s2[0:-1]
            return 1 +self.lcs_rec(s1[0:-1],s2[0:-1])
        else:
            return max(self.lcs_rec(s1[0:-1],s2),self.lcs_rec(s1,s2[0:-1]))

    def longestCommonSubsequence(self, text1, text2):

        print(self.lcs_dp(text1,text2))


if __name__ == "__main__":
    sol = Solution()

    text1 = "abc"
    text2 = "abc"
    sol.longestCommonSubsequence(text1, text2)
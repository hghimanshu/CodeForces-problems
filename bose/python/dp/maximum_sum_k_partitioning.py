class Solution:


    def getSum(self,arr,k):

        dp = [float("-inf")]*len(arr)
        dp[0] = arr[0]

        for i in range(1,len(arr)):
            j=1
            while j<=k and (i-j+1)>=0:
                length = j
                subarray = arr[i-j+1:i+1]
                max_val = length*max(subarray)
                if i-j<0:
                    dp[i] = max(dp[i],max_val)
                else:
                    dp[i] = max(dp[i],max_val+dp[i-j])
                j+=1

        return dp[i]


    def maxSumAfterPartitioning(self, arr, k):
        return self.getSum(arr,k)

if __name__ == "__main__":
    sol = Solution()
    arr = [1,4,1,5,7,3,6,1,9,9,3]
    k = 4
    print(sol.maxSumAfterPartitioning(arr,k))
from functools import lru_cache
class Solution:

    def __init__(self):
        self.lis = 0
        self.cache={}




    def getSeqDp(self,arr):
        lis = [1]*len(arr)
        count = [1]*len(arr)

        for i in range(1,len(arr)):
            for j in range(0,i):
                if arr[i] > arr[j]:
                    if lis[j]+1 > lis[i]: # we are trying to check if adding another number increases the sequence length:
                        lis[i] = lis[j]+1
                        count[i] = count[j]
                    elif lis[i] == lis[j]+1: # we find that even after adding a new element, the sequence length remanins the same. 
                        count[i]+=count[j]

        print(lis)
        print(count)
        max_val = max(lis)
        # if max_val > 1:
        #     max_val = max_val-1
        
        cnt=0
        for i in range(0,len(lis)):
            if lis[i] == max_val:
                cnt+=count[i]
        return cnt

    @lru_cache
    def getSeqMemo(self,idx,prev):

        # if idx in self.cache:
        #     return self.cache[idx]

        if idx!=prev:
            if self.arr[idx] <= self.arr[prev]:
            # if val <= self.arr[start] or val <= curr[-2]:
                return 0

        print("Current is {} and prev is {}".format(self.arr[idx], self.arr[prev]))
        totalSeq = 0
        
        for i in range(idx+1,len(self.arr)):
            totalSeq = max(totalSeq,self.getSeqMemo(i,idx))
            

        # self.cache[idx]=totalSeq+1

        return totalSeq+1

    def getSeq(self,curr,val,idx,start):

        # if (idx,val) in self.cache:
        #     return self.cache[(idx,val)]
        
        if idx!=start:
            if val <= self.arr[start] or val <= curr[-2]:
                return 0

        print("Start is {} Curr is :: {}".format(start,curr))
        self.lis = max(len(curr),self.lis)

        for i in range(idx+1,len(self.arr)):
            curr.append(self.arr[i])
            self.getSeq(curr,self.arr[i],i,start)
            curr.pop()
        
        return 


    def lengthOfLIS(self, nums):

        self.arr = nums

        return self.getSeqDp(nums)

        # for i in range(0,len(self.arr)):
        #     # self.getSeq([self.arr[i]],self.arr[i],i,i)
        #     self.lis = max(self.getSeqMemo(i,i),self.lis)
        #     if self.lis == len(nums):
        #         break
        
        # return self.lis

if __name__ == "__main__":
    sol = Solution()

    nums = [1,3,5,4,7]

    print(sol.lengthOfLIS(nums))

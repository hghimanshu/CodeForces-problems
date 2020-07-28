class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 1
        self.x = n
        self.count=1
        while(self.x):
            self.result^=1
            if self.result==0:
                self.count+=1
            self.x&=(self.x-1)
        return self.count

num = Solution()
print(num.hammingWeight(8))
class Solution:

    def __init__(self):
        self.permutations = []
        self.count= 0

    def checkIfBeautiful(self,perm):
        for i in range(0,len(perm)):
            if perm[i] % (i+1) == 0 or (i+1) % perm[i] == 0:
                continue
            else:
                return False
        return True


    def getPermutations(self,visited,perm,n,nums):

        if len(perm) == n:
            if self.checkIfBeautiful(perm):
                self.count+=1
                # self.permutations.append(perm.copy())
                return

        for j in range(0,len(nums)):
            if not visited[j] and (nums[j] % (len(perm)+1) == 0 or (len(perm)+1)%nums[j]==0):
                visited[j] = True
                perm.append(nums[j])
                self.getPermutations(visited,perm,n,nums)
                perm.pop()
                visited[j] = False

    
    def countArrangement(self,n):
        visited = [False]*n
        nums = [int(i+1) for i in range(0,n)]

        perm = []
        self.getPermutations(visited,perm,n,nums)

        return self.count

if __name__ == "__main__":
    sol = Solution()
    print(sol.countArrangement(3))
    # print(sol.checkIfBeautiful([3,1,2]))
    # print(sol.checkIfBeautiful([2,1,3]))
class Solution:

    def __init__(self):
        self.permutations = []

    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.backtrack(n, 1, [])
        print(self.permutations)
        return self.count
        
    def backtrack(self, N, idx, temp):
        if len(temp) == N:
            self.permutations.append(temp.copy())
            self.count += 1
            return
        
        for i in range(1, N+1):
            if i not in temp: #and (i % idx == 0 or idx % i == 0):
                temp.append(i)
                self.backtrack(N, idx+1, temp)
                temp.pop()

sol = Solution()
sol.countArrangement(3)


from collections import namedtuple

class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def traverseAndGetSum(self, root, sum_array, currentSum):
        if root:
            currentSum += str(root.data)
            if root.left is None and root.right is None:
                sum_array.append(currentSum)
                currentSum = 0
                return sum_array, currentSum
            
            self.traverseAndGetSum(root.left, sum_array, currentSum)
            self.traverseAndGetSum(root.right, sum_array, currentSum)
        
        return sum_array, currentSum


    def convertToBinary(self, array):
        return [int(i,2) for i in array]

    def sum(self, root):
        if root:
            all_sums = []
            all_sums, _ = self.traverseAndGetSum(root, all_sums, '')
            binary_list = self.convertToBinary(all_sums)

            return binary_list



            

    

## [1, 0,1,0,1,0,1,None,1,0,None,0,0,None,0,1,0,None, 1,None,0]

root = Tree(1)
root.left = Tree(0)
root.right = Tree(1)
root.left.left = Tree(0)
root.left.right = Tree(1)
root.left.left.left = Tree(0)
root.left.left.right = Tree(1)
root.left.right.right = Tree(1)
root.left.right.right.left = Tree(0)

root.right.left = Tree(0)
root.right.right = Tree(0)
root.right.left.right = Tree(0)
root.right.right.right = Tree(0)
root.right.left.right.left = Tree(1)
root.right.left.right.right = Tree(0)
root.right.left.right.left.right = Tree(1)


ans = Solution()
print(ans.sum(root))
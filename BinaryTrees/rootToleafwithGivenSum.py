from collections import namedtuple

class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root, s):
        if root is None:
            return False
        
        if not root.left and not root.right:
            return s == root.data

        return self.hasPathSum(root.left, s-root.data) or self.hasPathSum(root.right, s-root.data) 



            

    

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
print(ans.hasPathSum(root, 3))
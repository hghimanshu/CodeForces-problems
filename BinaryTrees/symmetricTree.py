class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def symmetricLogic(self, root1, root2):
        if root2 is None and root1 is None:
            return True
        
        if root1 is not None and root2 is not None:
            return (root1.data == root2.data) and self.symmetricLogic(root1.left, root2.right) and self.symmetricLogic(root1.right, root2.left)

    def checkSymmetric(self, root):
        if root is None:
            return True
        
        return self.symmetricLogic(root, root)

## [1,2,2,3,4,4,3]
root = Tree(1)
root.left = Tree(2)
root.right = Tree(2)
root.left.left = Tree(3)
root.left.right = Tree(4)
root.right.left = Tree(4)
root.right.right = Tree(3)


ans = Solution()
print(ans.checkSymmetric(root))
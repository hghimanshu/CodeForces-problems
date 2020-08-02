class Tree:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def preOrder(self, root, array):
        if root:
            ## Root --> Left --> Right
            array.append(root.data)
            self.preOrder(root.left, array)
            self.preOrder(root.right, array)
        return array
    
    def postOrder(self, root, array):
        if root:
            ## Left --> Right --> Root
            self.postOrder(root.left, array)
            self.postOrder(root.right, array)
            array.append(root.data)
        return array
    
    def inOrder(self, root, array):
        if root:
            ## Left --> Root --> Right
            self.inOrder(root.left, array)
            array.append(root.data)
            self.inOrder(root.right, array)
        return array
    

## [314, 6,6,271,561,28,0,None,3,17,None,2,271,None,1,None,28,401,257,None,641]

root = Tree(314)
root.left = Tree(6)
root.right = Tree(6)
root.left.left = Tree(271)
root.left.right = Tree(561)
root.left.left.left = Tree(28)
root.left.left.right = Tree(0)
root.left.right.right = Tree(3)
root.left.right.right.left = Tree(17)

root.right.left = Tree(2)
root.right.right = Tree(271)
root.right.left.right = Tree(1)
root.right.right.right = Tree(28)
root.right.left.right.left = Tree(401)
root.right.left.right.right = Tree(257)
root.right.left.right.left.right = Tree(641)


ans = Solution()
print("INORDER Traversal :: " + str(ans.inOrder(root, [])))
print("PREORDER Traversal :: " + str(ans.preOrder(root, [])))
print("POSTORDER Traversal :: " + str(ans.postOrder(root, [])))
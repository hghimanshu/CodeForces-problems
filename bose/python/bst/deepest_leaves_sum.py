from Tree_latest import BST,BinaryTreeNode

class Solution:

    def __init__(self):
        self.max_height = 0
        self.leafSum = 0

    def sumOfNodesAtMaxHeight(self,root,height):
        if height == self.max_height:
            self.leafSum+=root.data

        if not root.left and not root.right: #leaf nodes
            return
        

        if root.left:
            self.sumOfNodesAtMaxHeight(root.left,height+1)

        if root.right:
            self.sumOfNodesAtMaxHeight(root.right,height+1)


    def getMaxHeight(self,root,height):
        self.max_height = max(height,self.max_height)

        if not root.left and not root.right:
            return

        if root.left:
            self.getMaxHeight(root.left,height+1)

        if root.right:
            self.getMaxHeight(root.right,height+1)



    def deepestLeavesSum(self, root):

        #let's get the max height first
        self.getMaxHeight(root,0)
        print("Max height is ::{}".format(self.max_height))

        self.sumOfNodesAtMaxHeight(root,0)

        print("Sum of deepest leaves ::{}".format(self.leafSum))

if __name__ == "__main__":
    bst = BST() 
    print(bst)
    bst.push(15)
    bst.push(10)
    bst.push(4)
    bst.push(25)
    bst.push(17)
    bst.push(35)
    bst.push(30)
    bst.push(40)
    bst.push(8)
    bst.push(6)
    bst.push(12)
    # bst.inorder(bst.root)
    soln = Solution()
    soln.deepestLeavesSum(bst.root)
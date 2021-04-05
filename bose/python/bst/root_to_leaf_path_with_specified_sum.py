from Tree_latest import BST,BinaryTreeNode
def getMaxPathSum(root,path_sum):
    

    def getPathSum(root,current_sum):

        current_sum+=root.data
        if not root.left and not root.right: #leaf nodes
            
            return current_sum == path_sum

        if root.left:
            left_sum = getPathSum(root.left,current_sum)
        else:
            left_sum = False
        
        if root.right:
            right_sum = getPathSum(root.right,current_sum)
        else:
            right_sum = False     

        return left_sum + right_sum   

    leafPresent = getPathSum(root,0)

    return leafPresent

if __name__ == "__main__":
    bst = BST()  
    print(bst)
    bst.push(12)
    bst.push(8)
    bst.push(15)
    bst.push(13)
    bst.push(20)
    bst.push(17)
    bst.push(50)
    print(getMaxPathSum(bst.root,40))
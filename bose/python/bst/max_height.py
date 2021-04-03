from Tree_latest import BST,BinaryTreeNode


def maxDepth(node,height):

    if not node:
        return height
    
    height+=1

    left_height = maxDepth(node.left,height)
    right_height = maxDepth(node.right,height)

    return max(left_height,right_height)


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
    print("Max depth is :: {}".format(maxDepth(bst.root,0)))
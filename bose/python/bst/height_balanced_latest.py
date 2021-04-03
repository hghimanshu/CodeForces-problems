from Tree_latest import BST,BinaryTreeNode

def isHeightBalancedBruteForce(root):

    node_dict = {}

    def checkHeight(root):

        if not root:
            return 0

        l_h = checkHeight(root.left)
        r_h = checkHeight(root.right)

        node_dict.update({root.data:abs(l_h-r_h)})

        return 1+max(l_h,r_h)

    checkHeight(root)

    for k,v in node_dict.items():
        if v>1:
            return False
        
    return True
    

def isHeightBalancedOptimized(root):

    def checkHeight(root):
        if not root:
            return {"status":True,"val":0}



        left = checkHeight(root.left)
        right = checkHeight(root.right)

        
        # if left["status"] and right["status"]:
        #     return {"status":True,"val":1+max(left["val"],right["val"])}

        if not left["status"] or not right["status"]:
            return {"status":False,"val":1+max(left["val"],right["val"])}
        
        if abs(left["val"]-right["val"]) > 1:
            return {"status":False,"val":1+max(left["val"],right["val"])}
        else:
            return {"status":True,"val":1+max(left["val"],right["val"])}


    return checkHeight(root)["status"]


if __name__ == "__main__":
    bst = BST() 
    print(bst)
    bst.push(12)
    bst.push(8)
    bst.push(9)
    bst.push(6)
    # bst.push(7)
    bst.push(1)
    bst.push(15)
    # bst.push(13)
    # bst.push(20)
    # bst.push(17)
    # bst.push(50)
    # bst.push(45)
    # bst.push(55)
    # bst.push(51)
    # bst.push(60)
    print("Height balanced status of tree is:: {}".format(isHeightBalancedBruteForce(bst.root)))
    



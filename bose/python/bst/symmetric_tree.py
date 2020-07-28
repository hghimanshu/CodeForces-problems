from bst_deletion import TreeNode, BST



def checkIfMirror(root1,root2):
    if not root1 and not root2:
        return True

    if (root1 and root2) and (root1.key and root2.key):
        return checkIfMirror(root1.left_child,root2.right_child) and
               checkIfMirror(root1.right_child,root2.left_child)
    return False



bst1 = BST()
print(bst1)
# nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
nodes_to_insert = [9,7,8,5,6,4,10]

for node in nodes_to_insert:
    bst1.put(node)

checkIfBalanced(bst1.root)
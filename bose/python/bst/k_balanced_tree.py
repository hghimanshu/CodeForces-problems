from bst_deletion import TreeNode, BST


class BalancedStatus:
    def __init__(self,is_balanced,height,key):
        self.is_balanced = is_balanced
        self.height = height
        self.key = key


def checkIfBalanced(current_node,k):
    if not current_node:
        return BalancedStatus(True,-1,None)
        
    left_result = checkIfBalanced(current_node.left_child,k)
    if not left_result.is_balanced:
        #Left subtree is not balanced
        return BalancedStatus(False,0,current_node.key)
    right_result = checkIfBalanced(current_node.right_child,k)
    if not right_result.is_balanced:
        return BalancedStatus(False,0,current_node.key)

    is_balanced = abs(left_result.height - right_result.height) <= k
    height = max(left_result.height , right_result.height) + 1
    return BalancedStatus(is_balanced,height,current_node.key)





bst1 = BST()
print(bst1)
# nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
nodes_to_insert = [12,17,20,30,19,14,13,15,7,9,8,10,11,6]

for node in nodes_to_insert:
    bst1.put(node)

height_to_check = 1

print(checkIfBalanced(bst1.root,height_to_check).is_balanced)


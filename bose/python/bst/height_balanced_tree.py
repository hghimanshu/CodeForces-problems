from bst_deletion import TreeNode, BST


class BalancedStatus:
    def __init__(self,is_balanced,height):
        self.is_balanced = is_balanced
        self.height = height


def checkIfBalanced(current_node):
    if not current_node:
        return BalancedStatus(True,-1)
        
    left_result = checkIfBalanced(current_node.left_child)
    if not left_result.is_balanced:
        #Left subtree is not balanced
        return BalancedStatus(False,0)
    right_result = checkIfBalanced(current_node.right_child)
    if not right_result.is_balanced:
        return BalancedStatus(False,0)

    is_balanced = abs(left_result.height - right_result.height) <= 1
    height = max(left_result.height , right_result.height) + 1
    return BalancedStatus(is_balanced,height)





bst1 = BST()
print(bst1)
# nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
nodes_to_insert = [9,7,8,5,6,4,10]

for node in nodes_to_insert:
    bst1.put(node)

checkIfBalanced(bst1.root)


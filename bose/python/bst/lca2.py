from bst_deletion import TreeNode, BST


def LCA(root,key1,key2):
    if root is None:
        return None
    
    if root.key == key1 or root.key==key2:
        return root

    left_result = LCA(root.left_child,key1,key2) #check if key exists in left subtree.
    right_result = LCA(root.right_child,key1,key2) #check if key exits in right subtree

    if left_result and right_result:
        return root
    
    if left_result and not right_result:
        return left_result
    else:  #this condition ensures that something gets returned (even if both are None)
        return right_result




bst1 = BST()
# print(bst1)
nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
# nodes_to_insert = [9,7,8,5,6,4,10]


for node in nodes_to_insert:
    bst1.put(node)

print("LCA is ::: ",LCA(bst1.root,1,15).key)
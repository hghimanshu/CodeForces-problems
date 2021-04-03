def lca(root,node1,node2):
    if root:
        if root!=node1 and root!=node2:
            return root

    if not root:
        return None

    if root == node1 or root == node2:
        return root
    
    left =  lca(root.left,node1,node2)
    if left:
        if left!=node1 and left!=node2:
            return left
    right = lca(root.right,node1,node2)

    if left and right:
        return root

    if not left and not right:
        return None
    
    if left and not right:
        return left
    else:
        return right



from Tree_latest import BST,BinaryTreeNode


def iterative_inorder(node):
    result = []
    visited = []
    while visited or node:
        if node:
            visited.append(node)
            node = node.left
        else:
            node = visited.pop()
            result.append(node.data)
            node = node.right
    
    return result
    
def iterative_preorder(node):
    visited = [node]
    result = []
    while visited:
        curr = visited.pop()
        if curr:
            result.append(curr.data)
            visited+=[curr.right,curr.left]
    return result


def iterative_postorder(node):
    if not node:
        return []
    
    path, prev, postorder_sequence = [node],None,[]

    while path:
        curr = path[-1]
        if not prev or prev.left is curr or prev.right is curr:
            if curr.left: #Traverse left
                path.append(curr.left)
            elif curr.right: #Traverse right
                path.append(curr.right)
            else: #leaf nodes
                postorder_sequence.append(curr.data)
                path.pop()
        elif curr.left is prev: #Traverse the right subtree 
            if curr.right: 
                path.append(curr.right)
            else:
                # no right child so visit curr
                postorder_sequence.append(curr.data) 
                path.pop()
        else: #
            #finished travelling left and right, so visit curr
            postorder_sequence.append(curr.data)
            path.pop()
        prev = curr

    return postorder_sequence          

if __name__ == '__main__':
    bst = BST() 
    print(bst)
    bst.push(12)
    bst.push(8)
    bst.push(10)
    bst.push(9)
    bst.push(11)
    bst.push(4)
    bst.push(5)
    bst.push(15)
    bst.push(13)
    bst.push(17)
    bst.push(16)
    bst.push(1)
    print(iterative_postorder(bst.root))
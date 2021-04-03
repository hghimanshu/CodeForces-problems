from Tree_latest import BST,BinaryTreeNode


def level_order_traversal(node):
    if not node:
        return []
    
    result =[]
    level_result =[]
    
    visited = []
    curr_level =0
    prev_level=-1

    node = (node,curr_level)
    while node[0] or visited:
        if node[0]:
            curr_level = node[1]
            if curr_level!=prev_level:
                if level_result:
                    result.append(level_result)
                level_result = []
            level_result.append(node[0].data)
           
        # else:
        #     result.append(None)
        #     if visited:
        #         node = visited.pop(0)
        #         continue

        if node[0].left:
            visited.append((node[0].left,curr_level+1))
        # else:
        #     visited.append(None)
       

        if node[0].right:
            visited.append((node[0].right,curr_level+1))
        # else:
        #     visited.append(None)
        
        if visited:
            node = visited.pop(0)
        else:
            node = (None,None)
            result.append(level_result)
        prev_level =curr_level
        
    return result

if __name__ == '__main__':
    bst = BST() 
    print(bst)
    # bst.push(12)
    # bst.push(8)
    # bst.push(10)
    # bst.push(9)
    # bst.push(11)
    # bst.push(4)
    # bst.push(5)
    # bst.push(15)
    # bst.push(13)
    # bst.push(17)
    # bst.push(16)
    # bst.push(1)
    bst.push(1)
    # bst.push(9)
    # bst.push(20)
    # bst.push(15)
    # bst.push(22)
    
    print(level_order_traversal(bst.root))

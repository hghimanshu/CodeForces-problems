from bst_deletion import TreeNode, BST



def getVisitedNodes(key,currentNode,visitedNodes):
    if currentNode.key == key:
        visitedNodes.append(key)
        print("visited Nodes are:: ",visitedNodes)
        return visitedNodes
    if key> currentNode.key:
        print("Greater than current node")
        visitedNodes.append(currentNode.key)
        currentNode = currentNode.right_child
        return getVisitedNodes(key,currentNode,visitedNodes)
    if key<currentNode.key:
        print("Smaller than current node")
        visitedNodes.append(currentNode.key)
        currentNode = currentNode.left_child
        return getVisitedNodes(key,currentNode,visitedNodes)




def checkForLCA(key1,key2,root):
    key1visited = getVisitedNodes(key1,root,[])
    key2visited = getVisitedNodes(key2,root,[])
    print("key 1 visited nodes are::")
    print(key1visited)
    print("key 2 visited nodes are:::")
    print(key2visited)
    lca = 999999
    for visitedNode in key1visited:
        if visitedNode in key2visited:
            if visitedNode < lca:
                lca = visitedNode
    return lca




bst1 = BST()
# print(bst1)
nodes_to_insert = [8,4,5,6,7,3,2,1,15,11,10,13,12,14,17,16,18]
# nodes_to_insert = [9,7,8,5,6,4,10]


for node in nodes_to_insert:
    bst1.put(node)

print("LCA is ::: ",checkForLCA(4,1,bst1.root))


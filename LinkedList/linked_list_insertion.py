
class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def printList(self, L):
        while L:
            print(L.data)
            L = L.next

    def insertAfterTail(self, L, value):
        if L.next:
            self.insertAfterTail(L.next, value)
        else:
            L.next = LinkNode(value)
        
        return L


    def insertAfterAgivenNode(self, node, new_node, L):
        # new_node.next = node.next
        # node.next = new_node

        # return node

        if L:
            if L.data == node.data:
                new_node.next = node.next
                node.next = new_node
            self.insertAfterAgivenNode(node, new_node, L.next)
        
        return L
    
    def insertAfterHead(self, L, node):
        node.next = L.next
        L.next = node
        return L



# [1 --> 2 --> 4 --> 6]
node = LinkNode(1)
node.next = LinkNode(2)
node.next.next = LinkNode(4)
node.next.next.next = LinkNode(6)


ans = Solution()
L = ans.insertAfterTail(node, 9)
ans.printList(L)

print("\n\n")
L = ans.insertAfterAgivenNode(node.next, LinkNode(10), node)
ans.printList(L)


print("\n\n")
L = ans.insertAfterHead(node, LinkNode(15))
ans.printList(L)

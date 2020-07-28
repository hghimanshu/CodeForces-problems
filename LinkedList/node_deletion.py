
class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def printList(self, L):
        while L:
            print(L.data)
            L = L.next
    
    def deleteHead(self, L):
        del L.data
        L = L.next    
        return L

    def deleteTail(self, L):
        if L.next.next:
            self.deleteTail(L.next)
        else:
            L.next = None
        
        return L

    def deleteAgivenNode(self, node, L):
        if L.next:
            if L.next.data == node.data:
                L.next = node.next
            
            self.deleteAgivenNode(node, L.next)
        
        return L





# [1 --> 2 --> 4 --> 6]
node = LinkNode(1)
node.next = LinkNode(2)
node.next.next = LinkNode(4)
node.next.next.next = LinkNode(6)


ans = Solution()
# L = ans.deleteHead(node)
# ans.printList(L)

# print("\n\n")
# L = ans.deleteTail(L)
# ans.printList(L)

print("\n\n")
L = ans.deleteAgivenNode(node.next.next,node)
ans.printList(L)
